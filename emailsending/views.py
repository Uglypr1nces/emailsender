from django.shortcuts import render
from django.http import HttpResponse
from .python_functions.emailsender import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request, 'base.html')

def send_email(request):
    if request.method == 'POST':
        self_email = request.POST.get('self_email')
        email = request.POST.get('reciever_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(f'Email sent from {self_email} to {email} with subject {subject} and message {message}')
        send(self_email,email, subject, message)
        return HttpResponse('Email Sent')
