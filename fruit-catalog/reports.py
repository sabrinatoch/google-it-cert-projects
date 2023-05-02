#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles['h1'])
    report_content = Paragraph(paragraph, styles['BodyText'])
    blank = Spacer(1, 20)
    report.build([report_title, blank, report_content, blank])
