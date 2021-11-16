from django.urls import path

from posts.views import PostDetail


urlpatterns = [
    path('<slug>/', PostDetail.as_view(), name='post-detail'),
]