# Generated by Django 5.0.1 on 2024-02-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_bloguser_blog_user_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='blog_user_title',
            field=models.CharField(default='Graphics Designer | Programmer', max_length=250),
        ),
    ]
