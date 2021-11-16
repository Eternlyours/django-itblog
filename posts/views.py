from django.views.generic import detail

from posts.models import Post


class PostDetail(detail.DetailView):
    model = Post
    template_name = 'post-detail.html'

