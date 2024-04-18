from django.shortcuts import render
from django.views.generic import TemplateView



class SistemIndexView(TemplateView):
    template_name = 'analytic/index.html'