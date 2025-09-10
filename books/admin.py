from django.contrib import admin
from books.models import Category, Book, Review, BorrowRecord
# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(BorrowRecord)
