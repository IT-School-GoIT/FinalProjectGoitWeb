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
    files = File.objects.filter(user=request.user)
    return render(request, 's3_storage/file_list.html', {'files': files})


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
