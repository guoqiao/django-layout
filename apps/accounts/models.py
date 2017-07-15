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
