from dataclasses import replace
from datetime import date
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
        # races = list(Race.objects.filter(circuit=circuit).values_list('id', flat=True))
        # races_in_circuit = list(Result.objects.filter(race__in=races, grid=1).values_list('id', flat=True))
        # print(races_in_circuit)
        poles = pd.DataFrame(
            Result.objects.filter(race__circuit=circuit, grid=1).values("driver", "driver__lname", "race__circuit"))

        try:
            dif_poles = poles.groupby("driver__lname").value_counts().reset_index(name="poles").sort_values("poles",
                                                                                                            ascending=False)
        except:
            dif_poles = pd.DataFrame()
        results_wins = pd.DataFrame(
            Result.objects.filter(race__circuit=circuit, position=1).values("driver__fname", "driver__lname"))
        results_wins['driver_name'] = results_wins["driver__fname"] + '-' + results_wins["driver__lname"]
        results_wins = results_wins.drop(columns=['driver__fname', 'driver__lname'])
        top_winners = results_wins.groupby("driver_name").value_counts().reset_index(name='wins').sort_values('wins',
                                                                                                              ascending=False)
        top_winners = top_winners.sort_values('wins', ascending=False)

        data = {"circuit": circuit,
                "total_races": len(poles),
                "different_poles": len(dif_poles),
                "different_winners": len(top_winners),
                }

        return data


class CircuitDetailAPIView(APIView):
    def get(self, request, format=None):

        circuit = Circuit.objects.get(pk=int(request.GET.get('circuit')))
        results_wins = pd.DataFrame(Result.objects.filter(race__circuit=circuit, position=1).values("driver__fname", "driver__lname", "race__year"))
        results_wins['driver_name'] = results_wins["driver__fname"] + ' ' + results_wins["driver__lname"]
        start_year = results_wins['race__year'].min()
        end_year = results_wins['race__year'].max()
        results_wins = results_wins.drop(columns=['race__year', 'driver__fname', 'driver__lname'])

        top_winners = results_wins.groupby("driver_name").value_counts().reset_index(name='wins').sort_values('wins', ascending=False)
        top_winners = top_winners.sort_values('wins', ascending=False)

        data = []
        labels = []
        for index, row in top_winners.iterrows():
            labels.append(row["driver_name"])
            data.append(row["wins"])



        data = {
            "data": data,
            "labels": labels,
        }

        return Response(data)

class CircuitDnfDetailAPIView(APIView):
    def get(self, request, format=None):

        circuit = Circuit.objects.get(pk=int(request.GET.get('circuit')))
        completed_status_id = [1, 11, 88, 45, 55, 53, 111, 112, 116, 50, 114, 124, 12, 127, 120, 115, 119, 117, 113, 58,
                               118, 13, 123, 134, 14, 128, 122, 125, 133, 15, 16, 17, 18, 19, 97]
        results = pd.DataFrame(Result.objects.filter(race__circuit=circuit).exclude(status__in=completed_status_id).values("driver__fname", "driver__lname", "race__year", "status", "status__name"))
        results['driver_name'] = results["driver__fname"] + ' ' + results["driver__lname"]
        results = results.drop(columns=['driver__fname', 'driver__lname'])
        dnfs_by_year = results.groupby("race__year").size().reset_index(name='DNFs')

        data = []
        labels = []
        for index, row in dnfs_by_year.iterrows():
            labels.append(row["race__year"])
            data.append(row["DNFs"])

        type = ['line']
        data = {
            "data": data,
            "labels": labels,
            "type": type
        }

        return Response(data)



