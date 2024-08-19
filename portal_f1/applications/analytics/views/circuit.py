from django.views.generic import ListView, DetailView
from analytics.filters.circuit import CircuitFilter
from analytics.models.circuits import Circuit
from rest_framework.views import APIView

class CircuitDetailView(DetailView):
    template_name = 'circuit/circuit_detail.html'
    model = Circuit

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


class CircuitDetailAPIView(APIView):
    def get(self, request, format=None):
        circuit = Circuit.objects.get(pk=int(request.GET.get('circuit')))

        data = {}

        return Response(data)

