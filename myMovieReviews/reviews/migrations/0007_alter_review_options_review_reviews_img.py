# Generated by Django 5.0.7 on 2024-07-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_review_options_alter_review_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['title', 'year', 'director', 'actor', 'genre', 'star', 'time', 'newreview']},
        ),
        migrations.AddField(
            model_name='review',
            name='reviews_img',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
    ]
