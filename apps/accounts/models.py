from django.db import models
from django.contrib.auth.models import User, UserManager
from annoying.fields import AutoOneToOneField


class UserProxyManager(UserManager):

    def active_users(self):
        """Get active users"""
        return self.get_queryset().filter(is_active=True)


class UserProxy(User):
    """
    UserProxy is quite useful that you can add new methods to User without breaking anything.
    """
    class Meta:
        proxy = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    """
    Add new fields to User model here.
    """
    user = AutoOneToOneField(UserProxy)
    # TODO: add more fields here


class Preference(models.Model):
    """
    Generic key value preference for User
    """
    user = models.ForeignKey(UserProxy)
    group = models.CharField(max_length=100, default='')
    key = models.SlugField(max_length=100)
    value = models.TextField(blank=True)

    class Meta:
        unique_together = ('user', 'group', 'key')

    def __str__(self):
        return '[{}] {}={}'.format(self.group, self.key, self.value)
