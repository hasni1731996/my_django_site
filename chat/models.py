# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Userchat(models.Model):
    sender=models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender')
    reciver=models.ForeignKey(User, on_delete=models.CASCADE,related_name='reciver')
    message=models.CharField(max_length=100)
    created_at=models.DateTimeField()
    
    def __str__(self):
        return self.message