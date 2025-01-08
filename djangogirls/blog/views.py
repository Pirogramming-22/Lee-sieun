from django.shortcuts import render

# Create your views here.

def post_list(request): #요청을 넘겨받아 render메서드 호출
    return render(request, 'blog/post_list.html',{}) #render 메서드 호출하여 받은 blog/post)list.html 템플릿 보여줌

