# Generated by Django 2.0.1 on 2018-01-31 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('the_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count_views', models.IntegerField(default='0', verbose_name='总浏览')),
            ],
        ),
    ]
