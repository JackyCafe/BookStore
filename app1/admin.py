from django.contrib import admin
from app1.models import Books,Chapter


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Books._meta.fields]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Chapter._meta.fields]
