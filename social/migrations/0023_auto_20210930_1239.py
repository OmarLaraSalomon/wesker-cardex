# Generated by Django 3.1.2 on 2021-09-30 17:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0022_auto_20210930_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 9, 30, 12, 39, 23, 742101))),
                ('content', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 9, 30, 12, 39, 23, 742875))),
                ('content1', models.TextField()),
                ('user1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.RemoveField(
            model_name='postsalida',
            name='user_salida',
        ),
        migrations.DeleteModel(
            name='PostEntrada',
        ),
        migrations.DeleteModel(
            name='PostSalida',
        ),
    ]
