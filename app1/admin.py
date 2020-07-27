from django.contrib import admin
from app1.models import Post,Chapter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Post._meta.fields]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Chapter._meta.fields]
