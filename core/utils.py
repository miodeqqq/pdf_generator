# -*- coding: utf-8 -*-

import os
import time
import uuid

import pdfkit
from django.conf import settings
from django.core.files import File
from django.template import Template, Context


def prepare_directories(name):
    """
    Creates dirs and subdirs to avoid lack of space in storage.
    """

    data_dirs_datetime = str(time.strftime('%y/%m/%d/%H/%M'))

    file_path = os.path.join(
        '{media_root}/{dirname}/{data_dirs}'.format(
            dirname=name,
            media_root=settings.MEDIA_ROOT,
            data_dirs=data_dirs_datetime
        )
    )

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    return file_path


def reports_path(instance, filename):
    """
    Upload path for generated PDFs.
    """

    file_path = prepare_directories(name='pdf_reports')

    file_name, ext = os.path.splitext(filename)

    file_name = file_name.strip().lower().replace(' ', '_')

    return os.path.join(
        '{file_path}/{file_name}{ext}'.format(
            file_path=file_path,
            file_name=file_name,
            ext=ext
        )
    )


def generate_report_as_a_pdf(report_obj, html_source):
    """
    """

    pdfkit_options = {
        'page-size': 'Legal',
        'orientation': 'portrait',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': 'UTF-8',
        'no-outline': None,
        'print-media-type': '',
        'footer-right': '[page]'
    }

    pdf_file_name = f'{str(uuid.uuid4())[:10]}.pdf'

    try:
        html_source = bytes(
            html_source,
            encoding='utf-8',
            errors='ignore'
        )

        pdfkit.from_string(
            input=html_source.decode('utf-8'),
            output_path=pdf_file_name,
            options=pdfkit_options
        )
    except IOError as e:
        print(e)
        pass

    report_obj.pdf_output.save(
        pdf_file_name,
        File(open(pdf_file_name, 'rb')),
        save=False
    )

    report_obj.save()

    # Removes old copy
    if os.path.exists(pdf_file_name):
        os.remove(pdf_file_name)


def get_html_source(context, template_name):
    """

    """

    _template = os.path.join(settings.BASE_DIR, f'templates/{template_name}')

    try:
        html_template = Template(open(_template).read())

        html_source = html_template.render(Context(context))
    except IOError:
        html_source = 'HTML template called "{template}" doesn\'t exist.'

    return html_source
