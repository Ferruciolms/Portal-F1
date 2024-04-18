from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "sobreelena.html"

class AboutCPIDView(TemplateView):
    template_name = "CPID.html"