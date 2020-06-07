from django.shortcuts import render
from home import forms
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")



# class IndexView(TemplateView):
#     template_name = 'templates/index.html'

# class AboutView(TemplateView):
#     template_name = 'about.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['injectme'] = 'BASIC INJECTION!'
    #     return context


# class SchoolListView(ListView):
#     context_object_name = 'schools'
#     model = models.School


# class SchoolDetailView(DetailView):
#     context_object_name = 'school_detail'
#     model = models.School
#     template_name = 'home/school_detail.html'