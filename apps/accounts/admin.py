from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models as m


class PreferenceInline(admin.TabularInline):
    model = m.Preference
    fields = ['group', 'key', 'value']
    extra = 1


@admin.register(m.UserProxy)
class UserProxyAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
    inlines = [PreferenceInline]
