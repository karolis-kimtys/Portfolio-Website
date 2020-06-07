from django.contrib import admin
from .models import Experience
from tinymce.widgets import TinyMCE
from django.db import models
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ExperienceAdmin(SummernoteModelAdmin):

    fieldsets = [
        ("Order No.", {'fields': ["experience_order"]}),
        ("Section", {'fields': ["experience_section"]}),
        ("Company", {'fields': ["experience_company"]}),
        ("Job Title", {"fields": ["experience_job_title"]}),
        ("Date from", {'fields': ["date_from"]}),
        ("Date to", {'fields': ["date_to"]}),
        ("Content", {"fields": ["experience_content"]}),
    ]

    summernote_fields = '__all__'    

admin.site.register(Experience, ExperienceAdmin)