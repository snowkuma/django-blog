from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """A view that returns a rendered list of published posts."""
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, year, month, day, post):
    """A view that renders a posts detail if the request is valid.
    otherise it returns a 404 page."""
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
