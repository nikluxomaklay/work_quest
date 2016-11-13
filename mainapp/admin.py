# -*- coding: utf8 -*-
from django.contrib import admin
from mainapp.models import MsgModel


class AdminMsgModel(admin.ModelAdmin):
    list_display = ('user', 'is_sent', 'date_time')
    ordering = ('user', 'date_time', 'is_sent')


admin.site.register(MsgModel, AdminMsgModel)
