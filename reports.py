#!/usr/bin/env python3

 # reports.py

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate


def generate_report(pdf_doc, title, paragraph):
    # generate_report(attachment, title, paragraph)
  styles = getSampleStyleSheet()
  styleN = styles['Normal']
  styleH = styles['Heading1']
  story = []
  #add some flowables
  story.append(Paragraph(title,styleH))
  for line in paragraph.splitlines():
    if line == "":
      story.append(Spacer(1, 12))
    else:
      story.append(Paragraph(line,styleN))
  story.append(Spacer(1, 12))

  doc = SimpleDocTemplate(pdf_doc,pagesize = letter)
  doc.build(story)
  
