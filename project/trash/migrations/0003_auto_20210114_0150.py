# Generated by Django 3.1 on 2021-01-14 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0002_auto_20210114_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trash',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
