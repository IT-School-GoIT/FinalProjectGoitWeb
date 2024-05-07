import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class FileCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file_categories')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


def upload_to_s3(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f'uploads/{filename}'


def upload_avatar(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f'avatars/{filename}'


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    category = models.ForeignKey(FileCategory, on_delete=models.CASCADE, null=True, related_name='files')
    file = models.FileField(upload_to=upload_to_s3)
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.original_filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default_avatar.png', upload_to=upload_avatar)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
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