# Generated by Django 5.0.1 on 2024-02-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_bloguser_blog_user_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='blog_user_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]