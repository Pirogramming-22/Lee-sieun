from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

#post_list라는 view 가 루트 URL에 할당 -> 누군가 주소로 들어왔을 떄 viewx.post_list를 보여주라 함
#url 마다 고유의 name 짓는 것 중요

#post/<int:pk>/ : url 패턴 => post 문자 포함 & pk를 정수로 생각하고 뷰로 전송 & 다음에 / 한번 더 와야함
