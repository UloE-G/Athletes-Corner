# Generated by Django 3.2.25 on 2024-09-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
