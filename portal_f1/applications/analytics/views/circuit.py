from dataclasses import replace

from django.views.generic import ListView, DetailView
from analytics.filters.circuit import CircuitFilter
from analytics.models.circuits import Circuit
from rest_framework.views import APIView
from rest_framework.response import Response
from analytics.models.results import Result
from analytics.models.drivers import Driver
from analytics.models.races import Race
import pandas as pd
from analytics.models.qualifying import Qualifying
from analytics.models.qualify_3 import Qualify_3


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

class CircuitDetailView(DetailView):
    template_name = 'circuit/circuit_detail.html'
    model = Circuit

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context

    def get_object(self, queryset=None):
        circuit = Circuit.objects.get(pk=self.kwargs["pk"])
        races_in_circuit = pd.DataFrame(Race.objects.filter(circuit=circuit))
        poles = pd.DataFrame(Result.objects.filter(race__circuit=circuit, grid=1).values("driver", "race__circuit"))
        print(poles)

        try:
            dif_poles = poles.groupby("driver").value_counts().reset_index(name='poles')
        except:
            dif_poles = pd.DataFrame()
        results_wins = pd.DataFrame(Result.objects.filter(race__circuit=circuit, position=1).values("driver__fname", "driver__lname"))
        results_wins['driver_name'] = results_wins["driver__fname"] + '-' + results_wins["driver__lname"]
        results_wins = results_wins.drop(columns=['driver__fname', 'driver__lname'])
        top_winners = results_wins.groupby("driver_name").value_counts().reset_index(name='wins').sort_values('wins', ascending=False)
        top_winners = top_winners.sort_values('wins', ascending=False)
        print(top_winners)







        data = {"circuit": circuit,
                "total_races": len(races_in_circuit),
                "different_poles": len(dif_poles),
                "different_winners": len(top_winners),
                }


        return data




class CircuitDetailAPIView(APIView):
    def get(self, request, format=None):
        circuit = Circuit.objects.get(pk=int(request.GET.get('circuit')))


        data = {}

        return Response(data)

