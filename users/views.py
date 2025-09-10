from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.models import Author
from django.db.models import Count
from users.serializers import AuthorSerializer,AuthorCreateSerializer, AuthorDetailsSerializer

# Create your views here.
class AuthorViewSet(ModelViewSet):
    queryset=Author.objects.prefetch_related('authorBooks').annotate(book_count=Count('authorBooks')).all()
    serializer_class=AuthorSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST','PUT']:
            return AuthorCreateSerializer
        elif self.action=='retrieve':
            return AuthorDetailsSerializer
        return AuthorSerializer
