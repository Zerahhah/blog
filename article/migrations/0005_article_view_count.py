# Generated by Django 2.0.1 on 2018-01-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180123_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_count',
            field=models.IntegerField(default='0', verbose_name='点击数'),
        ),
    ]