import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class FileCategory(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="file_categories"
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        """
        The __str__ function is used to return a string representation of the object.
        This is useful for debugging and logging purposes, as well as for displaying
        the object in the interactive interpreter. The default implementation returns
        '&lt;%s instance at %s&gt;' % (self.__class__.__name__, id(self)), but you can override this behavior by defining your own __str__ method.
        
        :param self: Represent the instance of the class
        :return: The name of the class
        :doc-author: Trelent
        """
        return self.name


def upload_to_s3(instance, filename):
    """
    The upload_to_s3 function is a callback function that will be called when the model instance is saved.
    It takes two arguments: an instance of the model, and a filename. The function returns a string which 
    is used as the path to upload the file to S3.
    
    :param instance: Access the instance of the model that is being saved
    :param filename: Specify the name of the file that is being uploaded to s3
    :return: A string with the name of the file to be uploaded
    :doc-author: Trelent
    """
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f"uploads/{filename}"


def upload_avatar(instance, filename):
    """
    The upload_avatar function is a function that takes in an instance and filename.
    It then splits the filename into two parts, the extension and the name of the file.
    The extension is stored as ext, while uuid4() generates a random hexadecimal number 
    and stores it as filename. The return statement returns avatars/filename.
    
    :param instance: Get the user id and filename is used to get the file extension
    :param filename: Get the file name of the image
    :return: A string that is the path to the avatar
    :doc-author: Trelent
    """
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f"avatars/{filename}"


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")
    category = models.ForeignKey(
        FileCategory, on_delete=models.CASCADE, null=True, related_name="files"
    )
    file = models.FileField(upload_to=upload_to_s3)
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        The __str__ function is a special function in Python classes that defines
        how the object should be represented as a string. This is used by many of
        the print functions and str() to display information about the object.
        
        :param self: Represent the instance of the class
        :return: The original filename
        :doc-author: Trelent
        """
        return self.original_filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="default_avatar.png", upload_to=upload_avatar)

    def __str__(self):
        """
        The __str__ function is a special function in Python classes.
        It's the &quot;informal&quot; or nicely printable string representation of the object.
        This means that you can do:
        
        :param self: Represent the instance of the class
        :return: The username of the user
        :doc-author: Trelent
        """
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        """
        The save function is a function that saves the image to the database.
        It takes in two arguments, *args and **kwargs. The first argument is a tuple of positional arguments, 
        and second argument is a dictionary of keyword arguments.
        
        :param self: Refer to the current instance of the class
        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass keyworded, variable-length argument list to a function
        :return: The instance of the object
        :doc-author: Trelent
        """
        super().save()

        if self.avatar:
            img = Image.open(self.avatar)

            if img.height > 250 or img.width > 250:
                new_img = (250, 250)
                img.thumbnail(new_img)
                img_format = img.format  # Extract original image format
                img_name = f"{self.user.username}_{self.avatar.name.split('.')[0]}.{img_format.lower()}"
                temp_img = BytesIO()
                img.save(temp_img, format=img_format)
                temp_img.seek(0)
                self.avatar.save(img_name, ContentFile(temp_img.read()), save=False)

        super().save(*args, **kwargs)
