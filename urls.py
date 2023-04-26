''' 
from django.urls import path
from .views import BookView
from .views import register, login, logout
urlpatterns = [
    path('books/', BookView.as_view(), name='book-list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
]
'''
from django.urls import path
from .views import EmailLoginView

urlpatterns = [
    path('api/login/', EmailLoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]




  
