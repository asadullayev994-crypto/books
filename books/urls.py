from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import  BookListCreateGenericView, BookDetailGenericView,SignupView, BookModelViewSet,LogoutView


router = DefaultRouter()
router.register(r'books-set', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books-generic/', BookListCreateGenericView.as_view()),
    path('books-generic/<int:pk>/', BookDetailGenericView.as_view()),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', obtain_auth_token),
    path('logout/', LogoutView.as_view()),
    
]