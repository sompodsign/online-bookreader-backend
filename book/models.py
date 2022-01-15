import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Timing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(Timing, models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='books/', null=True, blank=True)
    author = models.CharField(max_length=255)
    description = models.TextField()
    edition = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    total_pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class BookDetail(Timing, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reader_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_details')
    page_number = models.IntegerField()

