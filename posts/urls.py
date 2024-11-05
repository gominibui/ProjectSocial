from django.urls import path

from .views import CreatePostView, AllPosts, post_detail

app_name = 'posts'

urlpatterns = [
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('all_posts/', AllPosts.as_view(), name='all_posts'),
    path('post_detail/', post_detail, name='post_detail'),
]