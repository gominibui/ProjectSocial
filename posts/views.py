from django.contrib.auth.middleware import get_user
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request

from .forms import CreatePostForm
from posts.models import Post
from django.contrib.auth.models import User

@method_decorator(login_required, name='dispatch')
class CreatePostView(View):
    def get(self, request):
        form = CreatePostForm()
        return render(request, 'create_post.html', {'form': form})

    def post(self, request):
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:all_posts')
        return render(request, 'create_post.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class AllPosts(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.all()


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_details.html', {'post': post})