from django.contrib import admin

from .models import User

# @admin.register
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name")

admin.site.register(User)
