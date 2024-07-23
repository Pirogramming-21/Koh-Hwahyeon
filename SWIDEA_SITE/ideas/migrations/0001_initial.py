# Generated by Django 5.0.7 on 2024-07-16 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='아이디어명')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y%m%d', verbose_name='Image')),
                ('explain', models.TextField(verbose_name='아이디어 설명')),
                ('interest', models.IntegerField(default=0, verbose_name='아이디어 관심도')),
                ('tool', models.CharField(max_length=30, verbose_name='예상 개발툴')),
            ],
        ),
    ]