from django.views.generic import TemplateView
import pandas as pd

from analytics.models.circuits import Circuit
from analytics.models.constructors import Constructor
from analytics.models.constructors_standings import ConstructorStanding
from analytics.models.drivers_standings import DriverStanding
from analytics.models.races import Race
from analytics.models.drivers import Driver


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        races = Race.objects.all()
        total_races = len(races)
        constructors = Constructor.objects.all()
        total_constructors = len(constructors)
        circuits = Circuit.objects.all()
        total_circuits = len(circuits)
        drivers = Driver.objects.all()
        total_drivers = len(drivers)
        cons_standing = pd.DataFrame(
            ConstructorStanding.objects.all().values('race__year', 'race__id', 'constructor', 'position'))
        last_race_year = cons_standing.loc[cons_standing.groupby("race__year")["race__id"].idxmax()]
        campeoes = set()
        for idx, row in last_race_year.iterrows():
            champion_wc = cons_standing[cons_standing.position == 1 & (cons_standing.race__id == row['race__id'])]
            campeoes.add(int(champion_wc.constructor.iloc[0]))

        driver_standing = pd.DataFrame(
            DriverStanding.objects.all().values('race__year', 'race__id', 'driver', 'position'))
        last_race_year = driver_standing.loc[driver_standing.groupby("race__year")["race__id"].idxmax()]

        campeoesDrivers = set()
        for idx, row in last_race_year.iterrows():
            driverChampion = driver_standing[driver_standing.position == 1 & (driver_standing.race__id == row['race__id'])]
            campeoesDrivers.add(int(driverChampion.driver.iloc[0]))


        context["drivers_wc"] = len(campeoesDrivers)
        context["constructors_wc"] = len(campeoes)
        context["total_constructors"] = total_constructors
        context["total_races"] = total_races
        context["total_circuits"] = total_circuits
        context["total_drivers"] = total_drivers

        return context


class GalleryView(TemplateView):
    template_name = 'main/gallery.html'


class CircuitView(TemplateView):
    template_name = 'main/circuits.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'
