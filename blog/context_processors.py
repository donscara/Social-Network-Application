from .models import Post


def get_total_posts(request):
    return {'get_total_posts': Post.objects.count()}
