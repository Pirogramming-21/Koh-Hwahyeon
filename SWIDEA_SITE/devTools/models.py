from django.db import models

# Create your models here.

class DevTool(models.Model):
    title=models.CharField('이름', max_length=30)
    type=models.CharField('종류', max_length=30)
    explain=models.TextField('개발툴 설명')

    def __str__(self):
        return f'{self.title}'