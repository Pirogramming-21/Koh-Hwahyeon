# Generated by Django 5.0.7 on 2024-07-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_alter_review_options_review_reviews_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['title', 'image', 'year', 'director', 'actor', 'genre', 'star', 'time', 'newreview']},
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviews_img',
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]