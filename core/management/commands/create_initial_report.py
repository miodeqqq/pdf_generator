# -*- coding: utf-8 -*-

from django.core.management import BaseCommand

from core.models import Report


class Command(BaseCommand):
    """
    External manage.py command

    Example of usage:
        ./manage.py create_initial_report
    """

    help = 'Creates initial report object.'

    def handle(self, *args, **options):
        """
        Override BaseCommand handle method.
        """

        report = Report.objects.create(
            title='Raport testowy - jakis tam opis'
        )

        report.save()
