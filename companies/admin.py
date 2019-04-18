# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
admin.site.register(Stock)

admin.site.register(realestatedata)
admin.site.register(richtext_field_test)
#admin.site.register(Profile)
admin.site.register(Multi_Users)
class Multi_UsersInline(admin.StackedInline):
    model = Multi_Users


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = (Multi_UsersInline,)