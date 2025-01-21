from django.shortcuts import get_object_or_404,render
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Post
from .forms import PostForm
import json


def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == 'POST':
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
        else :
            ctx = {
                'form':form,
            }
            return render(request, 'posts/post_new.html',ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'posts/post_new.html', ctx)
        

@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('id')
        post = get_object_or_404(Post, id=post_id)
        post.like += 1
        post.save()
        return JsonResponse({'success': True, 'likes': post.like})
    return JsonResponse({'success': False}, status=400)






from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    return render(request, 'posts/post_list.html', {'posts': posts, 'comment_form': comment_form})

def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return JsonResponse({
                'success': True,
                'author': comment.author,
                'content': comment.content,
                'id': comment.id
            })
    return JsonResponse({'success': False})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'success': True})
