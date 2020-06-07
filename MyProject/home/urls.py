from django.urls import path
from home import views


#Template tagging
app_name = 'home'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),   
    path('contact/', views.contact, name="contact"),   
]
