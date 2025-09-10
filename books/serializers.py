from rest_framework import serializers
from books.models import Book, Category, Review, BorrowRecord


class SimpleBookSerializer(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Book
        fields=['id','title','category','isbn',]

class BookSerializer(serializers.ModelSerializer):
    author=serializers.StringRelatedField()
    category=serializers.StringRelatedField()
    review_count=serializers.IntegerField(read_only=True)
    class Meta:
        model=Book
        fields=['id','title','author','isbn','category','availability_status','review_count']

class CategorySerializer(serializers.ModelSerializer):
    book_count= serializers.IntegerField(read_only=True)
    class Meta:
        model=Category
        fields=['id','name','description','book_count']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','user','book','content','rating']

class BorrowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowRecord
        fields=['id','book','member','borrow_date', 'return_date']