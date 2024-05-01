from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from .models import File, FileCategory
from .utils import delete_from_s3
from .forms import FileForm
from .custom_http_responses import HttpResponseConflict


@login_required
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        category_id = request.POST['category']
        category = FileCategory.objects.get(id=category_id)
        description = request.POST['description']
        file_obj = File.objects.create(
            file=file,
            category=category,
            user=request.user,
            original_filename=file.name,
            description=description
        )
        file_obj.save()
        return redirect('s3_storage:list')
    else:
        categories = FileCategory.objects.filter(user=request.user)
        return render(request, 'comander/upload.html', {'categories': categories})

@login_required
def file_list(request):
    categories = FileCategory.objects.filter(user=request.user)
    files = File.objects.filter(user=request.user)
    return render(request, 'comander/files.html', {
        'categories': categories,
        'files': files,
        'title': 'files',
        'page': 'files',
        'app': 's3_storage'
    })


@login_required
def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    response = HttpResponse(file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={file.original_filename}'
    return response


@login_required
def edit_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    if request.method == 'POST':
        form = FileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('s3_storage:list')
    else:
        form = FileForm(instance=file)
    return render(request, 's3_storage/edit_file.html', {'form': form})


@login_required
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    delete_from_s3(file.file.name)
    file.delete()
    return redirect('s3_storage:list')


@login_required
def create_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = FileCategory.objects.create(user=request.user, name=name)
        category.save()
        return redirect('s3_storage:category_list')
    else:
        return render(request, 's3_storage/add_category.html')


@login_required
def category_list(request):
    categories = FileCategory.objects.filter(user=request.user)
    return render(request, 's3_storage/all_categories.html', {'categories': categories})


@login_required
def edit_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('s3_storage:category_list')
    else:
        return render(request, 's3_storage/edit_category.html', {'category': category})


@login_required
@require_http_methods(['DELETE'])
def delete_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if category.files.exists():
        return HttpResponseConflict(content='Category cannot be deleted because it contains files.')
    else:
        category.delete()
        return JsonResponse({'message': 'Category has been deleted.'}, status=200)
