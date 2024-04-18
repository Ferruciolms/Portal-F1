from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from core_registration.models.company import Company
from core_registration.forms.company import CompanyForm
from core_registration.filters.company_filter import CompanyFilter
from core_log.save_db.create_log import save_log
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError

class CompanyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Company
    form_class = CompanyForm
    template_name = 'company/company.html'
    success_url = reverse_lazy('listar_company')
    permission_required = 'core_registration.add_company'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Cadastro de Empresa"
        context['bottom'] = 'Cadastrar'
        context['icone'] = '<i class="feather icon-log-out"></i>'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        new_company = Company.objects.get(pk=self.object.pk)
        save_log(new=new_company, user=self.request.user)
        return url

class CompanyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Company
    form_class = CompanyForm
    template_name = 'company/company.html'
    success_url = reverse_lazy('listar_company')
    permission_required = 'core_registration.change_company'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Editar Cadastro de Empresa"
        context['bottom'] = 'Salvar'
        return context
    
    def form_valid(self, form):
        old_company = Company.objects.get(pk=self.object.pk)
        url = super().form_valid(form)
        new_company = Company.objects.get(pk=self.object.pk)
        save_log(old=old_company, new=new_company, user=self.request.user)
        return url

class CompanyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_delete.html'
    success_url = reverse_lazy('listar_company')
    permission_required = 'core_registration.delete_company'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Company, pk=self.kwargs['pk'])
        return self.object
    
    def delete(self, request, *args, **kwargs):
        old_company = Company.objects.get(pk=self.kwargs['pk'])
        try:
            super().delete(request, *args, **kwargs)
            save_log(old=old_company, user=self.request.user)
        except ProtectedError:
            messages.error(request, f"Não foi possível remover \"{self.object}\", registro possui vínculo com outros cadastros.")
        return  HttpResponseRedirect(self.success_url)

class CompanyList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Company
    template_name = 'company/company_list.html'
    paginate_by = 10
    permission_required = 'core_registration.view_company'

    def dispatch(self, request, *args, **kwargs):
        return super(CompanyList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CompanyFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return CompanyFilter(self.request.GET, queryset=queryset).qs
