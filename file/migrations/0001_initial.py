# Generated by Django 4.1.3 on 2022-11-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("file", models.FileField(upload_to="file/uploaded_files")),
            ],
        ),
    ]
