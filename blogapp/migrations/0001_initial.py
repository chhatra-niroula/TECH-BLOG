# Generated by Django 5.0.1 on 2024-02-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_full_Name', models.CharField(max_length=50)),
                ('blog_user_email', models.CharField(max_length=50)),
                ('blog_username', models.CharField(max_length=50)),
                ('blog_user_created', models.CharField(max_length=50)),
                ('blog_user_isactive', models.BooleanField(default=False)),
                ('blog_user_modified', models.CharField(max_length=50)),
            ],
        ),
    ]
