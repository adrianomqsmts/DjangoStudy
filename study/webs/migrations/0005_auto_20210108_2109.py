# Generated by Django 3.1.5 on 2021-01-09 00:09

from django.db import migrations, models
import webs.models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0004_auto_20210108_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to=webs.models.user_post_directory_path),
        ),
    ]
