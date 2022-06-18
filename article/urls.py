from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='article-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='article-detail'),
    path('post/create/', PostCreateView.as_view(), name='article-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='article-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='article-delete'),
    path('my-articles/', views.mine, name='my-articles'),
]
