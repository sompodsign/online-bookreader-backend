from django.contrib import admin
from .models import Book, BookDetail


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader_id', 'book', 'page_number', 'created_at')


admin.site.register(Book, BookAdmin)
admin.site.register(BookDetail, BookDetailAdmin)

