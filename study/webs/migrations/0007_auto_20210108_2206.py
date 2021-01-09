# Generated by Django 3.1.5 on 2021-01-09 01:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webs', '0006_auto_20210108_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
