from django.db import models
from devTool.models import DevTool

class Ideas(models.Model):
    title = models.CharField('아이디어명', max_length=20)
    photo = models.ImageField('사진', blank=True, upload_to='ideas/')
    description = models.TextField('아이디어 설명')
    interest_rate = models.FloatField('아이디어 관심도')

    # DevTool의 이름을 선택 항목으로 사용하는 tool 필드
    TOOL_CHOICES = [(tool.name, tool.name) for tool in DevTool.objects.all()]
    tool = models.CharField(
        '예상 개발툴',
        max_length=50,
        choices=TOOL_CHOICES,
        default=None,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title