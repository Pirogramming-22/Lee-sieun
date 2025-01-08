from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #*models : Post가 장고 모델임을 알려줌 -> Post가 db에 저장되어야 함을 알게됨됨
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
        #* casacade : 관계형 db의 "연쇄 삭제" => 부모가 삭제되면 관련된 자식 객체도 함께 삭제
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null = True
    )

    def publish(self) :
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

#* models.CharField(max_length= ) : 글자수가 제한된 짧은 텍스트 (제목 같은)
#* models.TextField() : 글자수 제한 없는 긴 텍스트
#* models.DateTimeField() : 날짜와 시간
#* models.ForeignKey() : 다른 모델에 대한 링크