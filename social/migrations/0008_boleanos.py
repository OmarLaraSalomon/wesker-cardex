# Generated by Django 3.1.2 on 2022-06-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_boleano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='activate',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
