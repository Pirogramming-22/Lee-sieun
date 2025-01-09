from django.shortcuts import render,get_object_or_404, redirect
from .models import Post  #동일한 디렉토리 내에 있어서 .models로 호출
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def post_list(request): #요청을 넘겨받아 render메서드 호출
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')    #posts에 작성된 글의 목록이 들어감
    return render(request, 'blog/post_list.html',{'posts':posts}) #render 메서드 호출하여 받은 blog/post)list.html 템플릿 보여줌

def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)   #pk=pk 만족하는 객체 존재하면 반환, 존재하지 않으면 404에러페이지 반환
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":   #폼에서 받은 데이터가 있다면
        form = PostForm(request.POST) #가져온 데이터가 띄워져 있기
        if form.is_valid():
            post= form.save(commit=False)  #넘겨진 데이터를 바로 Post 모델에 저장X
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else :  #처음 페이지에 접속 ->  새 글 작성하게 폼이 비어있어야 함
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})