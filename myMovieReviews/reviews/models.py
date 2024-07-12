from django.db import models

# Create your models here.
GENRE=(
        ('액션','액션'),
        ("멜로/로맨스",'멜로/로맨스'),
        ("코미디",'코미디'),
        ("역사",'역사'),
        ("SF",'SF'),
        ("스릴러",'스릴러'),
        ("미스터리",'미스터리'),
        ("드라마",'드라마'),
        ("공포",'공포'),
        ("뮤지컬",'뮤지컬'),
        ("판타지",'판타지'),
        ("애니메이션",'애니메이션'),
        ("스포츠",'스포츠'),
        ("범죄",'범죄'),
    )

class Review(models.Model):
    title=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    year=models.CharField(max_length=5, null=True, blank=True)
    genre=models.CharField(max_length=10, choices=GENRE, default='로맨스')
    star=models.CharField(max_length=10, null=True, blank=True)
    time=models.CharField(max_length=10, null=True, blank=True)
    newreview=models.TextField(null=True, blank=True)
    director=models.CharField(max_length=10, null=True, blank=True)
    actor=models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering=['title','image','year','director','actor','genre','star','time','newreview']
