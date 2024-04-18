from django.contrib import admin
from analytics.models.circuits import Circuit
from analytics.models.constructors import Constructor
from analytics.models.constructors_results import ConstructorResult
from analytics.models.constructors_standings import ConstructorStanding
from analytics.models.drivers import Driver
from analytics.models.drivers_standings import DriverStanding
from analytics.models.fastest_lap import FastestLap
from analytics.models.lap_times import LapTime
from analytics.models.pit_stops import PitStop
from analytics.models.qualify_1 import Qualify_1
from analytics.models.qualify_2 import Qualify_2
from analytics.models.qualify_3 import Qualify_3
from analytics.models.qualifying import Qualifying
from analytics.models.races import Race
from analytics.models.results import Result
from analytics.models.results_times import ResultTime
from analytics.models.seasons import Season
from analytics.models.sprint_results import SprintResult
from analytics.models.sprint_results_times import SprintResultTime
from analytics.models.status import Status
from analytics.models.sprint_fastest_lap import SprintFastestLap
from analytics.models.free_practice import FreePractice
from analytics.models.qualify_session import QualifySession
from analytics.models.sprint_race import SprintRace

admin.site.register(Circuit)
admin.site.register(Constructor)
admin.site.register(Driver)
admin.site.register(Season)
admin.site.register(Race)
admin.site.register(ConstructorResult)
admin.site.register(ConstructorStanding)
admin.site.register(DriverStanding)
admin.site.register(LapTime)
admin.site.register(PitStop)
admin.site.register(Qualifying)
admin.site.register(Result)
admin.site.register(SprintResult)
admin.site.register(Status)
admin.site.register(Qualify_1)
admin.site.register(Qualify_2)
admin.site.register(Qualify_3)
admin.site.register(ResultTime)
admin.site.register(SprintResultTime)
admin.site.register(FastestLap)
admin.site.register(SprintFastestLap)
admin.site.register(FreePractice)
admin.site.register(SprintRace)
admin.site.register(QualifySession)
