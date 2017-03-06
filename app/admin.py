# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'boss', 'age', 'status']





