from django.shortcuts import render

# Create your views here.
def index_view(request):
    details = {'first_name': 'Tony', 'last_name': 'Izuogu', 'role': 'Software Engineer'}

    return render(request, 'first_app/index.html',context=details)
    

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