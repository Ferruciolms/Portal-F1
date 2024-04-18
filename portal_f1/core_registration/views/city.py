from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from core_registration.models.city import City
from core_registration.forms.city import CityForm
from core_registration.filters.city_filter import CityFilter
from core_log.save_db.create_log import save_log
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError

class CityCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = City
    form_class = CityForm
    template_name = 'city/city.html'
    success_url = reverse_lazy('list_city')
    permission_required = 'core_registration.add_city'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Cadastro de Cidade"
        context['bottom'] = 'Cadastrar'
        context['icone'] = '<i class="feather icon-log-out"></i>'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        new_city = City.objects.get(pk=self.object.pk)
        save_log(new=new_city, user=self.request.user)
        return url

class CityUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = City
    form_class = CityForm
    template_name = 'city/city.html'
    success_url = reverse_lazy('list_city')
    permission_required = 'core_registration.change_city'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Editar Cadastro de Cidade"
        context['bottom'] = 'Salvar'
        return context
    
    def form_valid(self, form):
        previous_city = City.objects.get(pk=self.object.pk)
        httpResponse = super().form_valid(form)
        new_city = City.objects.get(pk=self.object.pk)
        save_log(old=previous_city, new=new_city, user=self.request.user)
        return httpResponse

class CityDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = City
    form_class = CityForm
    template_name = 'city/city_delete.html'
    success_url = reverse_lazy('list_city')
    permission_required = 'core_registration.delete_city'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(City, pk=self.kwargs['pk'])
        return self.object
    
    def delete(self, request, *args, **kwargs):
        previous_city = City.objects.get(pk=self.kwargs['pk'])
        try:
            super().delete(request, *args, **kwargs)
            save_log(old=previous_city, user=self.request.user)
        except ProtectedError:
            messages.error(request, f"Não foi possível remover \"{self.object}\", registro possui vínculo com outros cadastros.")
        return  HttpResponseRedirect(self.success_url)

class CityList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = City
    template_name = 'city/city_list.html'
    paginate_by = 10
    permission_required = 'core_registration.view_city'

    def dispatch(self, request, *args, **kwargs):
        return super(CityList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CityFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return CityFilter(self.request.GET, queryset=queryset).qs
