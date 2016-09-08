# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  url(r'^$', views.index, name='index'),
                  url('^logout/$', views.logout, name='logout'),
                  url('^save_mail/$', views.save_mail, name='save_mail'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
