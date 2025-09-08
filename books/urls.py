from django.urls import path
from books.views import project_test
urlpatterns = [
    path('', project_test, name='test_view')
]
