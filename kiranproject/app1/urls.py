from . import  views
from django.urls import path

app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('fashion/',views.fashion,name='fashion'),
    path('personal/',views.personal,name='personal'),
    path('product/',views.product,name='product'),
    path('services/',views.services,name='services'),
    path('wedding/',views.wedding,name='wedding'),
]