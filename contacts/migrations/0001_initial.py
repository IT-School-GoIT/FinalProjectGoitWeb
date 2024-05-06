from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),  # Specify max_length for address field
                ('phone_number', models.CharField(max_length=15)),  # Remove validators for phone_number
                ('email', models.EmailField(max_length=254)),  # Remove validators for email
                ('birthday', models.DateField()),
                ('note', models.CharField(blank=True, null=True, max_length=255)),  # Specify max_length for note field
                ('user', models.ForeignKey(default=1, on_delete=models.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

