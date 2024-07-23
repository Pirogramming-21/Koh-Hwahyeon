from django.db import models
from apps.users.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    title=models.CharField(max_length=300)
    image=models.ImageField(upload_to='posts/%Y%m%d')
    text=models.TextField()
    like=models.IntegerField()
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

    def author_image(self):
        return self.author.profile_photo if self.author else None
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    writer=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content=models.TextField()
    created=models.DateTimeField(default=timezone.now, verbose_name="작성일")
    deleted=models.BooleanField(default=False, verbose_name="삭제여부")



