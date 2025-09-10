from rest_framework import serializers
from users.models import Member, Author
from books.serializers import SimpleBookSerializer

# class MemberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Member
#         fields=['first_name', 'last_name', 'email','address','phone_number', 'password']

class AuthorSerializer(serializers.ModelSerializer):
    book_count= serializers.IntegerField(read_only=True)
    class Meta:
        model=Author
        fields=['id','name','biography', 'book_count']

class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name','biography']

class AuthorDetailsSerializer(serializers.ModelSerializer):
    book_count= serializers.IntegerField(read_only=True)
    authorBooks=SimpleBookSerializer(many=True)
    class Meta:
        model=Author
        fields=['id','name','biography','book_count', 'authorBooks']
    
