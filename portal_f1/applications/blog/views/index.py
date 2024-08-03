from django.views.generic import TemplateView
import pandas as pd

from analytics.models.circuits import Circuit
from analytics.models.constructors import Constructor
from analytics.models.constructors_standings import ConstructorStanding
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
        # cons_standing = pd.DataFrame(list(ConstructorStanding.objects.all().values('race__year', 'race', 'constructor', 'points')))
        # print(cons_standing)







        context["total_constructors"] = total_constructors
        context["total_races"] = total_races
        context["total_circuits"] = total_circuits
        context["total_drivers"] = total_drivers

        return context


class GalleryView(TemplateView):
    template_name = 'main/gallery.html'

class CircuitView(TemplateView):
    template_name ='main/circuits.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'


