# Generated by Django 4.2.8 on 2024-05-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Currencies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bank_name", models.CharField(max_length=100)),
                ("buy_eur", models.CharField()),
                ("sell_eur", models.CharField()),
                ("buy_usd", models.CharField()),
                ("sell_usd", models.CharField()),
                ("pln_buy", models.CharField()),
                ("pln_sell", models.CharField()),
                ("url_link", models.URLField()),
            ],
        ),
    ]
