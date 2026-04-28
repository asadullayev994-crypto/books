from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookModelViewSet, BookListCreateGenericView, BookDetailGenericView


router = DefaultRouter()
router.register(r'books-set', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books-generic/', BookListCreateGenericView.as_view()),
    path('books-generic/<int:pk>/', BookDetailGenericView.as_view()),
]