from django.shortcuts import render
from . import models

# Create your views here.
def index_view(request):
    users = models.Register.objects.all()
    #details = {'first_name': 'Tony', 'last_name': 'Izuogu', 'role': 'Software Engineer'}
    users_list = {'register': users}

    return render(request, 'first_app/index.html',context=users_list)

def register_view(request):
    return render(request, 'first_app/register.html')
    
def how_view(request):
    return render(request, 'first_app/how_to_win.html')

def contact_view(request):
    return render(request, 'first_app/contact.html')

def quiz_view(request):
    return render(request, 'first_app/quiz.html')

def terms_view(request):
    return render(request, 'first_app/terms.html')

def faq_view(request):
    return render(request, 'first_app/faq.html')

def privacy_view(request):
    return render(request, 'first_app/privacy.html')