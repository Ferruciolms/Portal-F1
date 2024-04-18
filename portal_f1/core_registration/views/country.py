from datetime import datetime
from django.http import HttpResponseRedirect 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.db.models.deletion import ProtectedError
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from core_registration.models.country import Country
from core_registration.forms.country import CountryForm
from core_registration.filters.country_filter import CountryFilter
from core_log.save_db.create_log import save_log
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError

from django.contrib import messages

class CountryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Country
    form_class = CountryForm
    template_name = 'country/country.html'
    success_url = reverse_lazy('list_country')
    permission_required = 'core_registration.add_country'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Cadastro de País"
        context['bottom'] = 'Cadastrar'
        context['icone'] = '<i class="feather icon-log-out"></i>'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        new = Country.objects.get(pk=self.object.pk)
        save_log(new=new, user=self.request.user)
        return url

class CountryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Country
    form_class = CountryForm
    template_name = 'country/country.html'
    success_url = reverse_lazy('list_country')
    permission_required = 'core_registration.change_country'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Editar Cadastro de País"
        context['bottom'] = 'Salvar'
        return context

    def form_valid(self, form):
        previous_country = Country.objects.get(pk=self.object.pk)
        url = super().form_valid(form)
        new = Country.objects.get(pk=self.object.pk)
        save_log(old=previous_country, new=new, user=self.request.user)
        return url

class CountryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Country
    form_class = CountryForm
    template_name = 'country/country_delete.html'
    success_url = reverse_lazy('list_country')
    permission_required = 'core_registration.delete_country'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Country, pk=self.kwargs['pk'])
        return self.object

    def delete(self, request, *args, **kwargs):
        previous_country = Country.objects.get(pk=self.kwargs['pk'])
        try:
            super().delete(request, *args, **kwargs)
            save_log(old=previous_country, user=self.request.user)
        except ProtectedError:
            messages.error(request, f"Não foi possível remover \"{self.object}\", registro possui vínculo com outros cadastros.")
        return  HttpResponseRedirect(self.success_url)

class CountryList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Country
    template_name = 'country/country_list.html'
    paginate_by = 10
    permission_required = 'core_registration.view_country'

    def dispatch(self, request, *args, **kwargs):
        return super(CountryList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CountryFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return CountryFilter(self.request.GET, queryset=queryset).qs
