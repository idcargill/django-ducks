from django.views.generic import TemplateView
from .duck_form import DuckForm
from django.http import HttpResponse
from django.shortcuts import render

class HomePageView(TemplateView):
  template_name = 'home.html'


class AboutView(TemplateView):
  template_name = 'about.html'

