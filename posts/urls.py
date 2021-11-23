from django.urls import path

from posts.views import PostDetailView, PostListView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post-detail'),
]