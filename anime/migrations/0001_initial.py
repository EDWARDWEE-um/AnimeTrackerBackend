# Generated by Django 3.1.7 on 2021-05-11 15:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, unique=True)),
                ('type', models.CharField(max_length=250)),
                ('episodes', models.IntegerField(default=0)),
                ('image_url', models.TextField(default='')),
                ('url', models.TextField(default='')),
                ('synopsis', models.TextField(default='')),
                ('score', models.FloatField(default=0)),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.EmailField(max_length=254)),
            ],
        ),
    ]