# -*- coding:utf-8 -*-

from django.db import models
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=u"文章ID")
    title = models.CharField(max_length=200,verbose_name=u'标题')
    category = models.CharField(max_length=50,null=True,blank=True,default="",verbose_name=u"分类")
    body = models.TextField(verbose_name=u'内容')
    author = models.CharField(max_length=20,null=True,blank=True,default="",verbose_name=u"作者")
    pub_date = models.DateTimeField(default=timezone.now,verbose_name=u'发布时间')
    img_name = models.CharField(max_length=200,verbose_name=u"图片名称",default=" ")
    view_count = models.IntegerField(default='0',verbose_name=u"点击数")

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name=u"图片ID")
    img = models.ImageField(verbose_name=u"图片")

    def __unicode__(self):
        return self.title


class CountView(models.Model):
    the_date = models.DateField(default=timezone.now , verbose_name=u'日期')
    count_views = models.IntegerField(default='1',verbose_name=u'总浏览')

    def __unicode__(self):
        return self.count_views