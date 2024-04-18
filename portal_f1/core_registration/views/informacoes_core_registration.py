from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

class Informacoes_view(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'informacoes_core_registration.html'
    success_url = reverse_lazy('info_core_registration')

