import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from PIL import Image


class FileCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_categories')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def upload_to_s3(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f'uploads/{filename}'


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    category = models.ForeignKey(FileCategory, on_delete=models.CASCADE, null=True, related_name='files')
    file = models.FileField(upload_to=upload_to_s3)
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.original_filename


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png', upload_to='profile_images')

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
