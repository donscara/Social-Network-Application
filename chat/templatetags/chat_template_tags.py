from django import template
from django.contrib.auth.models import User

# internals

register = template.Library()


@register.inclusion_tag("chat/friendships.html")
def get_friendships(user=None):
    friendships = user.followed_friends.filter(is_friend_each_other=True)
    return {"friendships": friendships}
