from rest_framework import viewsets, generics, filters
from .models import Book
from .serializers import BookSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']


class BookListCreateGenericView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class BookDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer