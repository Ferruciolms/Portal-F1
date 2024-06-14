from django.shortcuts import render
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'main/index.html'


class GalleryView(TemplateView):
    template_name = 'main/gallery.html'

class CircuitView(TemplateView):
    template_name ='main/circuits.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


