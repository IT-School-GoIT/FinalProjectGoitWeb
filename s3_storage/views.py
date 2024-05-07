from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import File, FileCategory, Profile
from .utils import delete_from_s3
from .forms import FileForm, ProfileForm
from .custom_http_responses import HttpResponseConflict


@login_required
def upload_file(request):
    if request.method == "POST":
        file = request.FILES["file"]
        max_size = 10 * 1024 * 1024  # 10 MB in bytes
        if file.size > max_size:  # Check if the file size does not exceed 10 MB
            return render(
                request,
                "s3_storage/file_upload.html",
                {
                    "categories": FileCategory.objects.filter(user=request.user),
                    "error_message": "File size exceeds the maximum allowed size of 10 MB.",
                },
            )

        category_id = request.POST["category"]
        category = FileCategory.objects.get(id=category_id)
        description = request.POST["description"]
        file_obj = File.objects.create(
            file=file,
            category=category,
            user=request.user,
            original_filename=file.name,
            description=description,
        )
        file_obj.save()
        return redirect("s3_storage:list")
    else:
        categories = FileCategory.objects.filter(user=request.user)
        return render(
            request, "s3_storage/file_upload.html", {"categories": categories}
        )


@login_required
def file_list(request):
    categories = FileCategory.objects.filter(user=request.user)
    files = File.objects.filter(user=request.user)
    return render(
        request,
        "s3_storage/file_list.html",
        {
            "categories": categories,
            "files": files,
            "title": "files",
            "page": "files",
            "app": "s3_storage",
        },
    )


@login_required
def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    response = HttpResponse(file.file, content_type="application/force-download")
    response["Content-Disposition"] = f"attachment; filename={file.original_filename}"
    return response


@login_required
def edit_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    if request.method == "POST":
        form = FileForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect("s3_storage:list")
    else:
        form = FileForm(instance=file)
    return render(request, "s3_storage/file_edit.html", {"form": form})


@login_required
def delete_file(request, file_id):
    file = get_object_or_404(File, id=file_id, user=request.user)
    delete_from_s3(file.file.name)
    file.delete()
    return redirect("s3_storage:list")


@login_required
def create_category(request):
    if request.method == "POST":
        name = request.POST["name"]
        category = FileCategory.objects.create(user=request.user, name=name)
        category.save()
        return redirect("s3_storage:category_list")
    else:
        return render(request, "s3_storage/category_create.html")


@login_required
def category_list(request):
    categories = FileCategory.objects.filter(user=request.user)
    return render(request, "s3_storage/category_list.html", {"categories": categories})


@login_required
def edit_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if request.method == "POST":
        category.name = request.POST["name"]
        category.save()
        return redirect("s3_storage:category_list")
    else:
        return render(request, "s3_storage/category_edit.html", {"category": category})


@login_required
@require_http_methods(["DELETE"])
def delete_category(request, category_id):
    category = get_object_or_404(FileCategory, id=category_id, user=request.user)
    if category.files.exists():
        return HttpResponseConflict(
            content="Category cannot be deleted because it contains files."
        )
    else:
        category.delete()
        return JsonResponse({"message": "Category has been deleted."}, status=200)


@login_required
def profile(request):
    return render(
        request,
        "s3_storage/profile.html",
        {"title": "profile", "page": "profile", "app": "profile"},
    )


@login_required
def profile_settings(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Your profile is updated successfully")
            return redirect("s3_storage:profile_settings")

    else:
        profile_form = ProfileForm(instance=profile)

    return render(
        request, "s3_storage/profile_settings.html", {"profile_form": profile_form}
    )
