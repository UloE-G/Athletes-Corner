# Generated by Django 3.2.25 on 2024-09-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_review_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]
