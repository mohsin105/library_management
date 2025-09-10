from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from books.views import BookViewSet,ReviewViewSet, CategoryViewSet
from users.views import AuthorViewSet


router= routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)

book_router=routers.NestedDefaultRouter(router,'books', lookup='book')
book_router.register('reviews', ReviewViewSet, basename='reviews')


urlpatterns = [
    # path('books/', include('books.urls')),
    path('', include(router.urls)),
    path('', include(book_router.urls))
]
