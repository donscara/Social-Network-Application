from django.utils.safestring import mark_safe
from django import template
from django.db.models import Count

# internals
from ..models import Post

register = template.Library()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5, author=None):
    latest_posts = Post.objects.filter(author=author).order_by("-published_date")[:count]
    return {"latest_posts": latest_posts}


@register.simple_tag
def get_total_posts(user=None):
    return Post.objects.count()
