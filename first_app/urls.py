from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index_view,name='index'),
    path('how/',views.how_view,name='how'),
    path('contact/',views.contact_view,name='contact'),
    path('quiz/',views.quiz_view,name='quiz'),
    path('terms/',views.terms_view,name='terms'),
]