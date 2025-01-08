from django.shortcuts import render,get_object_or_404
from .models import Post  #동일한 디렉토리 내에 있어서 .models로 호출
from django.utils import timezone

def post_list(request): #요청을 넘겨받아 render메서드 호출
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')    #posts에 작성된 글의 목록이 들어감
    return render(request, 'blog/post_list.html',{'posts':posts}) #render 메서드 호출하여 받은 blog/post)list.html 템플릿 보여줌

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)   #pk=pk 만족하는 객체 존재하면 반환, 존재하지 않으면 404에러페이지 반환
    return render(request, 'blog/post_detail.html', {'post': post})
