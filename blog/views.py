from django.shortcuts import render
from django.http import Http404
from models import Post

def post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(request, 'post.html', {'post':post})
