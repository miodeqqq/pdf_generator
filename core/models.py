# -*- coding: utf-8 -*-

from django.db import models

from core.utils import reports_path


class Report(models.Model):
    """

    """

    title = models.CharField(
        verbose_name='Title',
        max_length=255,
        blank=True,
        null=True,
        db_index=True
    )

    created_dt = models.DateTimeField(
        verbose_name='Created',
        auto_now_add=True
    )

    pdf_output = models.FileField(
        'PDF',
        upload_to=reports_path,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
