from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

#post_list라는 view 가 루트 URL에 할당 -> 누군가 주소로 들어왔을 떄 viewx.post_list를 보여주라 함
#url 마다 고유의 name 짓는 것 중요

#post/<int:pk>/ : url 패턴 => post 문자 포함 & pk를 정수로 생각하고 뷰로 전송 & 다음에 / 한번 더 와야함
