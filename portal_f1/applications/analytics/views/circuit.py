from dataclasses import replace
from datetime import date
from django.views.generic import ListView, DetailView
from analytics.filters.circuit import CircuitFilter
from analytics.models.circuits import Circuit
from rest_framework.views import APIView
from rest_framework.response import Response

from analytics.models.fastest_lap import FastestLap
from analytics.models.lap_times import LapTime
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

        try:
            lap_times = pd.DataFrame(LapTime.objects.filter(race__circuit=circuit).values("race__year", "driver__fname","driver__lname", "mile_seconds"))
            lap_times["driver"] = lap_times["driver__fname"] + ' ' + lap_times["driver__lname"]
            lap_times = lap_times.drop(columns=['driver__fname', 'driver__lname'])
            lap_times["mile_seconds"] = pd.to_datetime(lap_times['mile_seconds'], unit='ms').dt.strftime(
                '%M:%S.%f').str[:-3]
        except:
            lap_times = pd.DataFrame()


        fastest_laps_by_year = []

        if not lap_times.empty:
            year_fastest_lap = lap_times.iloc[lap_times.groupby('race__year')['mile_seconds'].idxmin()]
            year_fastest_lap = year_fastest_lap.sort_values(by="race__year").reset_index(drop=True)
            min_time = year_fastest_lap['mile_seconds'].min()



            for index, row in year_fastest_lap.iterrows():
                new_row = {
                    'year': str(row['race__year']),
                    'time': row['mile_seconds'],
                    'driver': row['driver'],
                }
                if row['mile_seconds'] == min_time:
                    new_row['record'] = "record"
                fastest_laps_by_year.append(new_row)


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
                "race_laps": len(lap_times),
                "total_races": len(poles),
                "different_poles": len(dif_poles),
                "different_winners": len(top_winners),
                "record_year": fastest_laps_by_year,
                }


        return data


class CircuitDetailAPIView(APIView):
    def get(self, request, format=None):

        circuit = Circuit.objects.get(pk=int(request.GET.get('circuit')))
        results_wins = pd.DataFrame(Result.objects.filter(race__circuit=circuit, position=1).values("driver__fname", "driver__lname", "race__year"))
        results_wins['driver_name'] = results_wins["driver__fname"] + ' ' + results_wins["driver__lname"]
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
        not_dnf_status_id = [1, 11, 88, 45, 55, 53, 111, 112, 116, 50, 114, 124, 12, 127, 120, 115, 119, 117, 113, 58,
                               118, 13, 123, 134, 14, 128, 122, 125, 133, 15, 16, 17, 18, 19, 97, 81, 96]
        results = pd.DataFrame(Result.objects.filter(race__circuit=circuit).exclude(status__in=not_dnf_status_id).values("driver__fname", "driver__lname", "race__year", "status", "status__name"))
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



