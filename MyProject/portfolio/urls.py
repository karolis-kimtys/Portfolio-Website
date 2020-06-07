from django.urls import path, re_path
from portfolio import views
from .views import PortfolioListView, PortfolioDetailView

#Template tagging
app_name = 'portfolio'

urlpatterns = [
    # path('merger/', views.merger, name="merger"),
    path('portfolio/', PortfolioListView.as_view(), name='list'),
    re_path('(?P<pk>\d+)/', views.PortfolioDetailView.as_view(), name='detail'),
]