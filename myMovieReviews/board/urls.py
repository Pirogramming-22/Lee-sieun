from django.urls import path
from .views import *

app_name= 'board'

urlpatterns = [
    
    path('', board_list, name ='board_list'), #기본 페이지
    #리뷰 추가
    path('create', board_create, name ='board_create'),
    #리스트
    path('list', board_list, name ='board_list'),
    
    #업데이트
    path('update/<int:pk>', board_update, name ='board_update'),

    #디테일
    path('detail/<int:pk>', board_detail, name ='board_detail'),

    #삭제
    path('delete/<int:pk>', board_delete, name ='board_delete'),
]