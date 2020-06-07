from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render


class Experience(models.Model):

    SECTIONS = (
        (" ", " "),
        ("WORK EXPERIENCE", "WORK EXPERIENCE"),
        ("EDUCATION", "EDUCATION"),
        ("SKILLS", "SKILLS"),
    )

    experience_section = models.CharField(max_length = 50, choices = SECTIONS, default = "", blank=True)
    experience_company = models.CharField(max_length = 100, default = "", blank=True)
    date_from = models.CharField(max_length = 50, blank=True)
    date_to = models.CharField(max_length = 50, blank=True)
    experience_content = models.TextField(blank=True)
    experience_published = models.DateTimeField("date_published", auto_now_add=True, blank=True)
    experience_job_title = models.CharField(max_length = 200, blank=True)
    experience_order = models.CharField(max_length = 3, default = "0", blank=True)

    class Meta:
       ordering = ['experience_order']

    def __str__(self):
        return self.experience_job_title

    def get_absolute_url(self):
        return reverse("experience:detail",kwargs={'pk':self.pk})