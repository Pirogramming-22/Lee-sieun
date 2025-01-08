from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

#post_list라는 view 가 루트 URL에 할당 -> 누군가 주소로 들어왔을 떄 viewx.post_list를 보여주라 함
#url 마다 고유의 name 짓는 것 중요