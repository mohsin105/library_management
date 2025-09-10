from django.db import models
from users.models import Member,Author
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150)
    description= models.TextField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    STATUS_CHOICES=[
        ('AVAILABLE', 'Available'),
        ('BORROWED', 'Borrowed'),
        ('RESERVED', 'Reserved'),
        ('LOST', 'Lost'),
    ]
    title= models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete=models.CASCADE,related_name='authorBooks')
    isbn=models.CharField(max_length=13, unique=True, blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    availability_status=models.CharField(max_length=20,choices=STATUS_CHOICES, default='AVAILABLE')
    image=models.ImageField(upload_to='book_image/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    user=models.ForeignKey(Member,on_delete=models.CASCADE, related_name='userReviews')
    book= models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    content=models.TextField()
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


class BorrowRecord(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowRecord')
    member=models.ForeignKey(Member, on_delete=models.CASCADE, related_name='memberBorrowRecord')
    borrow_date=models.DateField(auto_now_add=True)
    return_date=models.DateField(auto_now_add=True)
# class Reservation(models.Model):
#     pass