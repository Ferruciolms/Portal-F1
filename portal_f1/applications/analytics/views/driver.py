import time
from datetime import date

import pandas as pd
from django.db.models import FloatField, Value, IntegerField, Min, CharField
from django.views.generic.list import ListView
from analytics.filters.driver import DriverFilter
from analytics.models.drivers import Driver
from analytics.models.races import Race
from analytics.models.results import Result
from django.views.generic import DetailView
from analytics.models.qualifying import Qualifying
from rest_framework.response import Response
from rest_framework.views import APIView
from analytics.models.drivers_standings import DriverStanding
from analytics.models.lap_times import LapTime
from analytics.models.circuits import Circuit


class DriverDetailView(DetailView):
    template_name = 'driver/driver_detail.html'
    model = Driver

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context
    def get_object(self, queryset=None):
        driver = Driver.objects.get(pk=self.kwargs["pk"])
        results = Result.objects.filter(driver=driver)
        pole = Qualifying.objects.filter(driver=driver, position=1)
        lap_times = pd.DataFrame(LapTime.objects.filter(driver=driver).values("lap", "race__year", "race__circuit","race__circuit__country", "race__circuit__id", "race__circuit__name", "mile_seconds"))
        lap_times = lap_times.iloc[lap_times.groupby("race__circuit")["mile_seconds"].idxmin()]
        lap_times['mile_seconds'] = pd.to_datetime(lap_times['mile_seconds'], unit='ms').dt.strftime('%M:%S.%f').str[:-3]
        lap_times = lap_times.sort_values(by="race__circuit__country").reset_index(drop=True)



        best_laps = []



        for row in lap_times.iterrows():
            circuit = Circuit.objects.get(pk=int(row[1]["race__circuit__id"]))
            try:
                flag_country = circuit.country_flag.url
            except:
                flag_country = ""
            lap_info = {
                "flag_country": flag_country,
                "lap": row[1]["lap"],
                "race__circuit__name": row[1]["race__circuit__name"],
                "race__circuit__country": row[1]["race__circuit__country"],
                "race__year": str(row[1]["race__year"]),
                "mile_seconds": row[1]["mile_seconds"]
            }

            best_laps.append(lap_info)




        completed_races = 0
        first_places = 0
        second_places = 0
        third_places = 0
        for result in results:
            if result.status.id == 1:
                if result.position == 1:
                    first_places += 1
                elif result.position == 2:
                    second_places += 1
                elif result.position == 3:
                    third_places += 1
                completed_races += 1



        data = {
            "pole": len(pole),
            "driver": driver,
            "total_races": len(results),
            "completed_races": completed_races,
            "first_places": first_places,
            "second_places": second_places,
            "third_places": third_places,
            "best_laps": best_laps,
                }

        return data


class DriverSeasonDetailAPIView(APIView):
    def get(self, request, format=None):
        driver = Driver.objects.get(pk=int(request.GET.get('driver')))
        results = pd.DataFrame(list(Result.objects.filter(driver=driver).values('points', 'race__year')))
        points = pd.DataFrame(results)


        start_year = results['race__year'].min()
        end_year = results['race__year'].max()



        years = []

        for i in range(start_year, end_year + 1):
            years.append(int(i))

        total_points = points.groupby('race__year')[['points']].sum().reset_index(names="race__year")

        points_year = []
        for year in years:
            try:
                points_year.append(total_points[(total_points['race__year'] == int(year))]['points'].iloc[0])
            except IndexError as e:
                points_year.append(0)


        points_by_year = [{'x': date(int(years[i]), 1, 1), 'y': points_year[i]} for i in range(0, len(years))]
        data = []

        data.append(points_by_year)

        labels = ["Total Points"]
        type = ['line']
        color = ['Lightblue']
        data = {
            "data": data,
            "labels": labels,
            "color": color,
            "type": type
        }

        return Response(data)


class DriverDetailAPIView(APIView):
    def get(self, request, format=None):

        driver = Driver.objects.get(pk=int(request.GET.get('driver')))
        results = pd.DataFrame(list(Result.objects.filter(driver=driver).values('position', 'race__year')))
        poles = pd.DataFrame(list(Qualifying.objects.filter(driver=driver, position=1).values('race__year')))
        positions = [1, 2, 3]
        podium = pd.DataFrame(Result.objects.filter(driver=driver, position__in=positions).values('position', 'race__year'))
        races = pd.DataFrame(results)

        position_dataframes = [df_position for position, df_position in podium.groupby('position')]

        dataframe_first = position_dataframes[0]
        dataframe_second = position_dataframes[1]
        dataframe_third = position_dataframes[2]



        start_year = results['race__year'].min()
        end_year = results['race__year'].max()


        years = []
        for i in range(start_year, end_year + 1):
            years.append(int(i))

        poles = poles.value_counts("race__year").reset_index(name='poles')
        poles = poles.sort_values('race__year')

        dataframe_first = dataframe_first.value_counts("race__year").reset_index(name='firsts')
        dataframe_first = dataframe_first.sort_values('race__year')

        dataframe_second = dataframe_second.value_counts("race__year").reset_index(name='seconds')
        dataframe_second = dataframe_second.sort_values('race__year')

        dataframe_third = dataframe_third.value_counts("race__year").reset_index(name='thirds')
        dataframe_third = dataframe_third.sort_values('race__year')

        races = races.value_counts("race__year").reset_index(name='races')
        races = races.sort_values('race__year')

        races_year = []
        poles_year = []
        firsts_year = []
        seconds_year = []
        thirds_year = []

        for year in years:
            try:
                poles_year.append(poles.loc[poles['race__year'] == int(year), 'poles'].iloc[0])
            except IndexError as e:
                poles_year.append(0)

            try:
                firsts_year.append(dataframe_first.loc[dataframe_first['race__year'] == int(year), 'firsts'].iloc[0])
            except IndexError as e:
                firsts_year.append(0)

            try:
                seconds_year.append(
                    dataframe_second.loc[dataframe_second['race__year'] == int(year), 'seconds'].iloc[0])
            except IndexError as e:
                seconds_year.append(0)

            try:
                thirds_year.append(
                    dataframe_third.loc[dataframe_third['race__year'] == int(year), 'thirds'].iloc[0])
            except IndexError as e:
                thirds_year.append(0)

            try:
                races_year.append(races.loc[races['race__year'] == int(year), 'races'].iloc[0])
            except IndexError as e:
                races_year.append(0)

        poles_by_year = [{'x': date(int(years[i]), 1, 1), 'y': poles_year[i]} for i in range(0, len(years))]
        firsts_by_year = [{'x': date(int(years[i]), 1, 1), 'y': firsts_year[i]} for i in range(0, len(years))]
        seconds_by_year = [{'x': date(int(years[i]), 1, 1), 'y': seconds_year[i]} for i in range(0, len(years))]
        thirds_by_year = [{'x': date(int(years[i]), 1, 1), 'y': thirds_year[i]} for i in range(0, len(years))]
        races_by_year = [{'x': date(int(years[i]), 1, 1), 'y': races_year[i]} for i in range(0, len(years))]

        data = []

        data.append(poles_by_year)
        data.append(firsts_by_year)
        data.append(seconds_by_year)
        data.append(thirds_by_year)
        data.append(races_by_year)


        labels = ['Poles', '1st', '2nd', '3rd', 'Races']
        type = ['line', 'line', 'line', 'line', 'bar']
        color = ['red', '#daa520', '#c0c0c0', '#cd7f32', 'rgba(255, 99, 132, 0.2)']


        data = {
            "data": data,
            "labels": labels,
            "color": color,
            "type": type
        }

        return Response(data)


class DriverList(ListView):
    model = Driver
    template_name = 'driver/driver_list.html'
    paginate_by = 10
    permission_required = 'analytics.view_driver'

    def dispatch(self, request, *args, **kwargs):
        return super(DriverList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = DriverFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        data = DriverFilter(self.request.GET, queryset=queryset).qs
        data = data.annotate(period=Value("None", output_field=CharField()))

        for driver in data:
            start = Result.objects.filter(driver=driver).order_by("race__year").values("race__year")
            year_start = start[0]["race__year"]
            year_final = start[len(start)-1]["race__year"]
            driver.period = str(year_start) + " - " + str(year_final)



        return data