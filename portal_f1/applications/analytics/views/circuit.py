from django.views.generic import ListView
from analytics.models.circuits import Circuit


class CircuitList(ListView):
    model = Circuit
    template_name = 'circuit/circuit_list.html'
    paginate_by = 10
    # permission_required = 'analytics.view_circuit'