# Generated by Django 5.0.7 on 2024-07-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='이름')),
                ('type', models.CharField(max_length=30, verbose_name='종류')),
                ('explain', models.TextField(verbose_name='개발툴 설명')),
            ],
        ),
    ]