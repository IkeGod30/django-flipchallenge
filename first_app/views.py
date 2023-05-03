from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def index_view(request):
    users = models.Register.objects.all()
    #details = {'first_name': 'Tony', 'last_name': 'Izuogu', 'role': 'Software Engineer'}
    users_list = {'register': users}

    return render(request, 'first_app/index.html',context=users_list)

def register_view(request):
    if request.POST:
        first = request.POST['first']
        last = request.POST['last']
        dob = request.POST['dob']
        email = request.POST['email']
        user = request.POST['user']
        password = request.POST['password']
        confirm = request.POST['confirm']
        models.Register.objects.create(first_name=first,last_name=last,dob=dob,email=email,user_name=user,password=password,confirm_password=confirm)
        return redirect(reverse('first_app:index'))
    else:
        return render(request,'first_app/register.html')
    
    #return render(request, 'first_app/register.html')

def success_view(request):
    return render(request, 'first_app/success.html')

def sign_in_view(request):
    return render(request, 'first_app/sign_in.html')
    
def how_view(request):
    return render(request, 'first_app/how_to_win.html')

def contact_view(request):
    return render(request, 'first_app/contact.html')

@login_required
def quiz_view(request):
    return render(request, 'first_app/quiz.html')

def terms_view(request):
    return render(request, 'first_app/terms.html')

def faq_view(request):
    return render(request, 'first_app/faq.html')

def privacy_view(request):
    return render(request, 'first_app/privacy.html')