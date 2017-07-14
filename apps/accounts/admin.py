from django.contrib import admin
from django.contrib.auth.models import UserAdmin
from . import models as m


@admin.register(m.UserProxy)
class UserProxyAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
