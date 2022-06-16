from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='article-home'),
    path('about/', views.about, name='article-about'),
]