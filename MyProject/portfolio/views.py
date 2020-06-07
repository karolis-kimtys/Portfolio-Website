from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpRequest
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from .models import Project
from . import models

# def portfolio(request):
#     return render(request = request,
#                   template_name='portfolio.html',
#                   context = {"project":Project.objects.all})


class PortfolioListView(ListView):
    context_object_name = 'project'
    model = models.Project

class PortfolioDetailView(DetailView):
    context_object_name = 'project_details'
    model = models.Project
    template_name = 'portfolio/project_detail.html'


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/merger.html', {
        'form': form
    })