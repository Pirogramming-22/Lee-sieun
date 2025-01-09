from django.contrib import admin
from .models import Post   #*models.py에 만들었던 Post를 가져옴
# Register your models here.

admin.site.register(Post)   #관리자 페이지에서 만든 보기 위해서 모델 등록

