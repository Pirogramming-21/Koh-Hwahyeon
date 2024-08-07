# Generated by Django 5.0.7 on 2024-07-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_actor_review_director_review_newreview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='genre',
            field=models.CharField(choices=[('ACTION', '액션'), ('ROMANCE', '멜로/로맨스'), ('COMEDY', '코미디'), ('HISTORY', '역사'), ('SF', 'SF'), ('THRILLER', '스릴러'), ('MYSTERY', '미스터리'), ('DRAMA', '드라마'), ('HORROR', '공포'), ('MUSICAL', '뮤지컬'), ('FANTASY', '판타지'), ('ANIMATION', '애니메이션'), ('SPORT', '스포츠'), ('CRIME', '범죄')], default='ROMANCE', max_length=10),
        ),
    ]
