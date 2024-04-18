from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = "site/index.html"

class IndexSystemView(TemplateView):
    template_name = "system/inicio.html"