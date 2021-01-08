from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return "profile/user_{id}/{file}".format(id=instance.user.id, file=filename)


GENDER_CHOICES = [
    ('N', 'Not specified'),
    ('M', 'Masculine'),
    ('F', 'Feminine'),
    ('O', 'Others'),
]
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    gender = models.CharField(choices=GENDER_CHOICES, default='Not specified', max_length=1)
    profile_pic = models.ImageField(upload_to=user_directory_path)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


@receiver(pre_save, sender=Profile)
def delete_old_file(sender, instance, **kwargs):
    # on creation, signal callback won't be triggered
    if instance._state.adding and not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).profile_pic
    except sender.DoesNotExist:
        return False
    # comparing the new file with the old one
    file = instance.profile_pic
    if not old_file == file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
