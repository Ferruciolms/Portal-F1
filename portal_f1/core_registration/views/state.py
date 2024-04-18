from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from core_registration.models.state import State
from core_registration.forms.state import StateForm
from core_registration.filters.state_filter import StateFilter
from core_log.save_db.create_log import save_log
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import ProtectedError

class StateCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = State
    form_class = StateForm
    template_name = 'state/state.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'core_registration.add_state'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Cadastro de Estado"
        context['bottom'] = 'Cadastrar'
        context['icone'] = '<i class="feather icon-log-out"></i>'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        url = super().form_valid(form)
        new = State.objects.get(pk=self.object.pk)
        save_log(new=new, user=self.request.user)
        return url

class StateUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = State
    form_class = StateForm
    template_name = 'state/state.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'core_registration.change_state'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = "Editar Cadastro de Estado"
        context['bottom'] = 'Salvar'
        return context
    
    def form_valid(self, form):
        previous_state = State.objects.get(self.object.pk)
        url = super().form_valid(form)
        new = State.objects.get(pk=self.object.pk)
        save_log(old=previous_state, new=new, user=self.request.user)
        return url

class StateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = State
    form_class = StateForm
    template_name = 'state/state_delete.html'
    success_url = reverse_lazy('list_state')
    permission_required = 'core_registration.delete_state'

    def get_object(self, queryset=None):
        self.object = get_object_or_404(State, pk=self.kwargs['pk'])
        return self.object
    
    def get_success_url(self) -> str:
        return super().get_success_url()
    
    def delete(self, request, *args, **kwargs):
        previous_state = State.objects.get(pk=self.kwargs['pk'])
        try:
            super().delete(request, *args, **kwargs)
            save_log(old=previous_state, user=self.request.user)
        except ProtectedError:
            messages.error(request, f"Não foi possível remover \"{self.object}\", registro possui vínculo com outros cadastros.")
        return  HttpResponseRedirect(self.success_url)

class StateList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = State
    template_name = 'state/state_list.html'
    paginate_by = 10
    permission_required = 'core_registration.view_state'

    def dispatch(self, request, *args, **kwargs):
        return super(StateList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StateFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return StateFilter(self.request.GET, queryset=queryset).qs
