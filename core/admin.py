# -*- coding: utf-8 -*-

from django.contrib import admin

from core.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """

    """

    list_display = (
        'title',
        'created_dt'
    )
