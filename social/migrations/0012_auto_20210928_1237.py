# Generated by Django 3.1.2 on 2021-09-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20210928_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
