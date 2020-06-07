"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', include('home.urls')),

    path('admin/', admin.site.urls),       #Used for Admin log in

    path('experience/', include('experience.urls')),
    path('signup/', include('registration.urls')), 
    path('portfolio/', include('portfolio.urls')), 
    path('tinymce/', include('tinymce.urls')),
    path('summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)