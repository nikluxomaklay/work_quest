# -*- coding: utf8 -*-
# from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MsgModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg_text = models.TextField(name='Message text')
    is_sent = models.BooleanField(name='Message sent', default=False)
    date_time = models.DateTimeField(name='Date of sent', auto_now_add=True)
