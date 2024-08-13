from django.views.generic import ListView
from django.db.models import FloatField, Value, IntegerField, Min, CharField
from analytics.filters.circuit import CircuitFilter
from analytics.models.circuits import Circuit
from analytics.models.results import Result


class CircuitList(ListView):
    model = Circuit
    template_name = 'circuit/circuit_list.html'
    paginate_by = 10
    permission_required = 'analytics.view_circuit'

    def dispatch(self, request, *args, **kwargs):
        return super(CircuitList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CircuitFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        data = CircuitFilter(self.request.GET, queryset=queryset).qs

        return data
