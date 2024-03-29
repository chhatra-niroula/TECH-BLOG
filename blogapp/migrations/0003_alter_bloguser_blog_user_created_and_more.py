# Generated by Django 5.0.1 on 2024-02-01 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_bloguser_blog_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='blog_user_created',
            field=models.DateTimeField(default=datetime.date),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='blog_user_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='blog_user_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
