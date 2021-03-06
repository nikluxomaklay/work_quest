# -*- coding: utf8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MsgModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg_text = models.CharField(max_length=255, blank=True)
    is_sent = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
