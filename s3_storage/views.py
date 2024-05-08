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
    """
    The upload_file function is responsible for handling the file upload process.
    It first checks if the request method is POST, which means that a form has been submitted.
    If it's not POST, then we render the file_upload template with all of our categories in it.
    If it's POST, then we get our category from the form and create a new File object with all of its attributes.
    
    :param request: Get the file from the form
    :return: A redirect to the list view
    :doc-author: Trelent
    """
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
    """
    The file_list function is a view that returns an HTML page with the list of files and categories for the current user.
    The file_list function takes in one parameter, request, which is a HttpRequest object.
    The file_list function returns an HttpResponse object containing the rendered template s3_storage/file_list.html.
    
    :param request: Get the current user
    :return: A list of the files that are uploaded to the s3 bucket
    :doc-author: Trelent
    """
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
    """
    The download_file function is used to download a file from the server.
    It takes in a request and file_id, and returns an HttpResponse object with the content of the file.
    
    
    :param request: Get the user from the request object
    :param file_id: Get the file object from the database
    :return: The file object as a response
    :doc-author: Trelent
    """
    file = get_object_or_404(File, id=file_id, user=request.user)
    response = HttpResponse(file.file, content_type="application/force-download")
    response["Content-Disposition"] = f"attachment; filename={file.original_filename}"
    return response


@login_required
def edit_file(request, file_id):
    """
    The edit_file function is used to edit a file.
    It takes in the request and the file_id of the file that needs to be edited.
    The function then gets the object or returns a 404 error if it does not exist.
    If there is an HTTP POST method, then we create a form with all of our data from our post request and instance=file (the current version).  We save this form if it's valid, otherwise we return an error message saying that something went wrong with saving your changes.  Otherwise, we just create a new FileForm instance.
    
    :param request: Get the request from the user
    :param file_id: Get the file object from the database
    :return: A render function
    :doc-author: Trelent
    """
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
    """
    The delete_file function takes a request and file_id as parameters.
    It gets the object or returns 404 if it doesn't exist. It then deletes the file from S3,
    and finally deletes the object from our database.
    
    :param request: Get the user and the file_id parameter is used to get a specific file
    :param file_id: Get the file object from the database
    :return: A redirect to the list view
    :doc-author: Trelent
    """
    file = get_object_or_404(File, id=file_id, user=request.user)
    delete_from_s3(file.file.name)
    file.delete()
    return redirect("s3_storage:list")


@login_required
def create_category(request):
    """
    The create_category function is used to create a new category for the user.
    The function first checks if the request method is POST, and if it is, then it creates a new FileCategory object with
    the name of the category being equal to what was entered in by the user. The function then saves this object and redirects
    to s3_storage:category_list.
    
    :param request: Get the request object, which contains information about the user and their session
    :return: A redirect to the category_list view
    :doc-author: Trelent
    """
    if request.method == "POST":
        name = request.POST["name"]
        category = FileCategory.objects.create(user=request.user, name=name)
        category.save()
        return redirect("s3_storage:category_list")
    else:
        return render(request, "s3_storage/category_create.html")


@login_required
def category_list(request):
    """
    The category_list function is a view that displays all of the categories
    that belong to the user. It takes in a request object and returns an HttpResponse
    object with the rendered template &quot;s3_storage/category_list.html&quot; and context 
    variable &quot;categories&quot;, which contains all of the FileCategory objects belonging 
    to this user.
    
    :param request: Get the user from the request object
    :return: A list of all the categories for a user
    :doc-author: Trelent
    """
    categories = FileCategory.objects.filter(user=request.user)
    return render(request, "s3_storage/category_list.html", {"categories": categories})


@login_required
def edit_category(request, category_id):
    """
    The edit_category function is used to edit the name of a category.
    It takes in a request and category_id as parameters, and returns an HttpResponse object.
    The function first gets the FileCategory object with id=category_id, or raises 404 if it doesn't exist.
    If the request method is POST, then we set the name of that FileCategory to be whatever was submitted in POST[&quot;name&quot;], save it, and redirect back to s3_storage:category_list (the list view). If not POST (i.e., GET), then we render out s3_storage/category_edit.html
    
    :param request: Get the current user
    :param category_id: Get the category object from the database
    :return: The category_edit
    :doc-author: Trelent
    """
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
    """
    The delete_category function deletes a file category.
    
    :param request: Get the user from the request object
    :param category_id: Find the category that is to be deleted
    :return: A jsonresponse with a message and status code 200 if the category is successfully deleted
    :doc-author: Trelent
    """
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
    """
    The profile function is used to render the profile.html template, which
    is a page that allows users to view and edit their profiles.
    
    :param request: Get the request object
    :return: The profile
    :doc-author: Trelent
    """
    return render(
        request,
        "s3_storage/profile.html",
        {"title": "profile", "page": "profile", "app": "profile"},
    )


@login_required
def profile_settings(request):
    """
    The profile_settings function is a view that allows the user to update their profile.
    The function first checks if the user has a profile, and if not, creates one for them.
    If the request method is POST (i.e., they are submitting an updated form), then it saves 
    the new information in their profile and redirects them back to this page with a success message.
    
    :param request: Get the user information
    :return: The profile_settings
    :doc-author: Trelent
    """
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
