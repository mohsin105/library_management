from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from books.models import Book,Category, Review, BorrowRecord
from books.serializers import BookSerializer, CategorySerializer, ReviewSerializer, BorrowRecordSerializer
from django.db.models import Count
# Create your views here.

@api_view()
def project_test(request):
    return Response({'message': 'Hello library management project'})

class BookViewSet(ModelViewSet):
    queryset=Book.objects.prefetch_related('reviews').annotate(
        review_count=Count('reviews')
    ).all()
    serializer_class=BookSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.annotate(book_count=Count('books', distinct=True)).all()
    serializer_class=CategorySerializer

class ReviewViewSet(ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer



