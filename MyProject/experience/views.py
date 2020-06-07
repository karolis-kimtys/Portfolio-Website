from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from .models import Experience
from . import models


# def experience(request):
#     return render(request, "experience.html")

class ExperienceListView(ListView):
    context_object_name = 'experience'
    model = models.Experience