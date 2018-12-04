# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        pass

class BjjydyArticle(models.Model):
    year_and_issue = models.CharField(u'年份期数', max_length=10)
    authors = models.CharField(u'作者', max_length=20)
    title = models.CharField(u'文章名称', max_length=50)
    school = models.CharField(u'所在学校', max_length=30)
    section = models.CharField(u'所在栏目', max_length=10)
    page_number = models.CharField(u'页码', max_length=10)
    remark = models.CharField(u'备注',blank=True, max_length=200)

    class Meta:
        verbose_name = u'北京教育（德育）文章'
        verbose_name_plural = u'北京教育（德育）文章'
        ordering = ['-year_and_issue', '-page_number']

    def __str__(self):
        return self.title


class Kt(models.Model):
    KT_TYPE_CHOICES = (
        ('01', '战略课题'),
        ('02', '重点课题'),
        ('03', '一般课题'),
        ('04', '支持课题'),
    )

    COMPLETED_CHOICES = (
        (True, '是'),
        (False, '否'),
    )

    year = models.IntegerField(u'申报年份')
    kt_type = models.CharField(u'课题类型', max_length=10, choices=KT_TYPE_CHOICES)
    project_number = models.CharField(u'项目编号', max_length=30)
    applicant = models.CharField(u'申报人', max_length=30)
    school = models.CharField(u'所在学校', max_length=70)
    kt_name = models.CharField(u'课题名称', max_length=100)
    is_completed_or_not = models.BooleanField(u'是否结项', choices=COMPLETED_CHOICES, default=False)
    remark = models.CharField(u'备注', blank=True, max_length=200)

    class Meta:
        verbose_name = u'课题'
        verbose_name_plural = u'课题'
        ordering = ['-year', 'project_number']

    def __str__(self):
        return self.kt_name