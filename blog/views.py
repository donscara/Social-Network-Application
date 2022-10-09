import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.views.generic import (
    ListView,
    CreateView,
)
from django.db.models import Q, Count

# internals.
from .forms import PostForm
from core.utils import elapsed_timer
from .models import Post
from .forms import SearchForm


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post/new.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


def post_list(request):
    ctx = {}
    allposts = Post.objects.order_by("-created_date")
    if request.user.is_authenticated:
        friend_ids = list(request.user.followed_friends.values_list("followed_id", flat=True))
        allposts = allposts.filter(author__id__in=[*friend_ids, request.user.id])

    paginator = Paginator(allposts, per_page=4)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(number=1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(number=paginator.num_pages)

    ctx.update(allposts.aggregate(total_post=Count("id")))
    ctx.update(
        {
            "page": page,
            "posts": posts,
        },
    )
    return render(request, "blog/post/list.html", ctx)


def post_detail(request, pk):
    def queryset():
        qs = Post.objects.all()
        return qs

    post = get_object_or_404(queryset(), pk=pk)
    context = {
        "post": post,
    }
    return render(request, "blog/post/detail.html", context)
