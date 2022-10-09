from django.urls import path
# internals
from . import views
from blog.feed import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post-list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.post_detail, name='post-detail'),
    
]
