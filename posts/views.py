from django.views.generic import detail
from django.views.generic import list

from posts.models import Post


class PostListView(list.ListView):
    model = Post
    template_name = 'post-list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.posts().only_active()


class PostDetailView(detail.DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.posts().only_active()

