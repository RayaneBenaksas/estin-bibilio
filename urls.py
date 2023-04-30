''' 
from django.urls import path
from .views import BookView
from .views import register, login, logout
urlpatterns = [
    path('books/', BookView.as_view(), name='book-list'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
# ]
# '''
# from django.urls import path
# from .views import EmailLoginView


# #from django.urls import path

# urlpatterns = [
#       
#     path('api/login/', EmailLoginView.as_view(), name='rest_login'),
#     #path('logout/', LogoutView.as_view(), name='logout'),

# ]
from knox import views as knox_views
from .views import RegisterAPI
from django.urls import path
from .views import LoginAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]





  
