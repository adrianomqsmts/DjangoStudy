from django.db import models
import os
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    return "profile/user_{id}/{file}".format(id=instance.user.id, file=filename)

def user_post_directory_path(instance, filename):
    return "profile/user_{id}/posts/{name}_{file}".format(id=instance.author.id, name=instance.title, file=filename)

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
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=user_post_directory_path, max_length=150, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    

    class Meta:
        """Meta definition for Post."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-post_date']

    def __str__(self):
        """Unicode representation of Post."""
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()

    def btn_name_like(self):
        return "btn-" + str(self.pk)

    def btn_name_comment(self):
        return "btn-comment-" + str(self.pk)


class Comment(models.Model):
    """Model definition for Comment."""

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comment_author", on_delete=models.CASCADE)
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Post."""
        return str(self.post) + ' commented : ' + str(self.author)



@receiver(pre_save, sender=Post)
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
