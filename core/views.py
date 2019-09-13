# -*- coding: utf-8 -*-

import os

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from core.models import Report
from core.utils import get_html_source, generate_report_as_a_pdf


class HomeView(TemplateView):
    """
    """

    def get(self, request, *args, **kwargs):
        """
        """

        html = f'''
        <html>
            <head>
                <h1 style="text-align:center;">Hello :) </h1>
            </head>
        <body>
            <center><a href="/report/1/"><b>See report 1</b></a></center>
        </body>
        </html>
        '''.strip()

        return HttpResponse(content_type='text/html', status=200, content=html)


class GeneratePdf(TemplateView):
    """

    """

    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        """
        """

        report = get_object_or_404(Report, pk=self.kwargs.get('report_pk'))

        html_source = get_html_source(
            context=self.get_context_data(),
            template_name=self.template_name
        )

        generate_report_as_a_pdf(
            report_obj=report,
            html_source=html_source
        )

        response = HttpResponse(
            content=report.pdf_output,
            content_type='application/pdf',
            status=200
        )

        # filename = os.path.basename(report.pdf_output.path)
        #
        # response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
