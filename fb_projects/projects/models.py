# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class FbProjects(models.Model):
    user = models.ForeignKey(User)
    domain = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    url_fb = models.CharField(max_length=2048)
    date_create = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"Проекты"
        db_table = u'fb_projects'
        app_label = 'projects'


class FbAccounts(models.Model):
    user = models.ForeignKey(User)
    fb_id = models.CharField(max_length=128, db_index=True)
    login = models.CharField(max_length=512)
    password = models.CharField(max_length=512)
    token = models.CharField(max_length=512)
    token_expired = models.DateTimeField(default=datetime.now)
    date_create = models.DateTimeField(default=datetime.now)

    app_id = models.CharField(max_length=256)
    app_secret = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u"Аккаунты"
        db_table = u'fb_accounts'
        app_label = 'projects'


class FbPages(models.Model):
    account = models.ForeignKey(FbAccounts)
    fb_id = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=512)
    category = models.CharField(max_length=512)
    access_token = models.CharField(max_length=512)
    email = models.CharField(max_length=512, null=True)

    class Meta:
        verbose_name = u"Страницы"
        db_table = u'fb_pages'
        app_label = 'projects'


class FbLeadgenForms(models.Model):
    page = models.ForeignKey(FbPages)
    fb_id = models.CharField(max_length=128, db_index=True)
    name = models.CharField(max_length=512)

    class Meta:
        verbose_name = u"Форма заявки"
        db_table = u'fb_leadgen_form'
        app_label = 'projects'


class FbLeads(models.Model):
    form = models.ForeignKey(FbLeadgenForms)
    fb_id = fb_id = models.CharField(max_length=128, db_index=True)
    date_receive = models.DateTimeField(default=datetime.now)
    created_time = models.DateTimeField(default=datetime.now)
    field_data = models.CharField(max_length=4096)
    email_send = models.DateTimeField(null=True)

    def __unicode__(self):
        return '{} {}'.format(self.form.page.name, self.created_time.strftime('%Y-%m-%d %H:%M:%S'))

    class Meta:
        verbose_name = u"Заявка"
        db_table = u'fb_lead'
        app_label = 'projects'
