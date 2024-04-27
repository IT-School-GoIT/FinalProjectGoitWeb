from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import File, FileCategory
from .utils import delete_from_s3


@login_required
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES['file']
        category_id = request.POST['category']
        category = FileCategory.objects.get(id=category_id)
        file_obj = File.objects.create(file=file, category=category, user=request.user, original_filename=file.name)
        file_obj.save()
        return redirect('s3_storage:list')
    else:
        categories = FileCategory.objects.filter(user=request.user)
        return render(request, 's3_storage/upload.html', {'categories': categories})

@login_required
def file_list(request):
    categories = FileCategory.objects.filter(user=request.user)
    files = File.objects.filter(user=request.user)
    # return render(request, 's3_storage/file_list.html', {'categories': categories, 'files': files})
    # return render(request, '_fragments/command_all_files.html', {'categories': categories, 'files': files})
    return render(request, 'comander/files.html', {
        'categories': categories,
        'files': files,
        'title': 'files',
        'page': 'files',
        # 'app': 'comander'
        'app': 's3_storage'
    })


@login_required
def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    response = HttpResponse(file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={file.original_filename}'
    return response


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
        return redirect('s3_storage:list')
    else:
        return render(request, 's3_storage/create_category.html')


@login_required
def edit_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('s3_storage:list')
    else:
        return render(request, 's3_storage/edit_category.html', {'category': category})


@login_required
def delete_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if category.files.exists():
        return render(request, 's3_storage/category_error.html', {'category': category})
    else:
        category.delete()
        return redirect('s3_storage:list')
# def delete_category(request, category_id):
#     category = get_object_or_404(FileCategory, id=category_id, user=request.user)
#     if category.file_set.exists():
#         return render(request, 's3_storage/category_error.html', {'category': category})
#     else:
#         category.delete()
#         return redirect('s3_storage:list')
