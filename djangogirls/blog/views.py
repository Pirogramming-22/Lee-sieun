from django.shortcuts import render
from .models import Post  #동일한 디렉토리 내에 있어서 .models로 호출
from django.utils import timezone

def post_list(request): #요청을 넘겨받아 render메서드 호출
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts}) #render 메서드 호출하여 받은 blog/post)list.html 템플릿 보여줌

