from django.db import models
from devTools.models import DevTool
# Create your models here.

class Idea(models.Model):
    title=models.CharField('아이디어명', max_length=30)
    image=models.ImageField('이미지', blank=True, upload_to='image/%Y%m%d')
    explain=models.TextField('아이디어 설명')
    interest=models.IntegerField('아이디어 관심도', default=0)
    tool=models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name='예상 개발툴')

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('idea',)