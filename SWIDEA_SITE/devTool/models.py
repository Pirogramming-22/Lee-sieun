from django.db import models

class DevTool(models.Model):
    name = models.CharField('이름', max_length=20)
    kind = models.CharField('종류',max_length=50)
    content = models.TextField('개발 툴 설명')