from django.contrib import admin
from .models import Project
from tinymce.widgets import TinyMCE
from django.db import models
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class ProjectAdmin(SummernoteModelAdmin):

    # fieldsets = [
    #     ("Title", {'fields': ["project_title"]}),
    #     ("Short Summary", {'fields': ["project_short_summary"]}),
    #     ("Summary", {'fields': ["project_summary"]}),
    #     ("Content", {"fields": ["project_content"]}),
    #     ("Author", {"fields": ["project_author"]}),
    #     ("GitHub Link", {"fields": ["project_github"]}),
    #     ("Image", {"fields": ["project_image"]}),
    # ]

    summernote_fields = '__all__'



        
admin.site.register(Project, ProjectAdmin)