# Generated by Django 3.1 on 2021-01-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0003_auto_20210114_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
