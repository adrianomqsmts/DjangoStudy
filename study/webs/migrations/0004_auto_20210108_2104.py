# Generated by Django 3.1.5 on 2021-01-09 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0003_auto_20210108_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
