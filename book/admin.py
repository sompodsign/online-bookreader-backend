from django.contrib import admin
from .models import Book, BookDetail


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


admin.site.register(Book, BookAdmin)
