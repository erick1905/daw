from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO, StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
import os

# Create your views here.
def reprte(request):
    response=HttpResponse(content_type='aplication/pdf')
    response['Conten-Disposition']= 'attachment; filename= report.pdf'
    buffer =BytesIO()
    c=canvas.Canvas(buffer, pagesize= A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750, 'Hola mundo')
    c.save()
    pdf=buffer.getvalue()
    buffer.write(pdf)
    return response

