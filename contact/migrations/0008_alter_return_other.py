# Generated by Django 3.2.25 on 2024-09-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_alter_return_reasons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='other',
            field=models.TextField(null=True),
        ),
    ]