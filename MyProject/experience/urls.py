from django.urls import path, re_path
from portfolio import views
from .views import ExperienceListView

#Template tagging
app_name = 'experience'

urlpatterns = [
    # path('experience/', views.experience, name="experience"),
    path('experience/', ExperienceListView.as_view(), name='list'),
    ]
