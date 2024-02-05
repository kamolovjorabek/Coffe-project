from django.contrib import admin
from news.models import (
    Category,
    New
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created_at', 'creator')
