from django.urls import path
from django.urls import re_path
from core_registration.views.informacoes_core_registration import Informacoes_view
from core_registration.views.company import CompanyCreateView, CompanyDeleteView, CompanyUpdateView, CompanyList
from core_registration.views.country import CountryCreateView, CountryUpdateView, CountryDeleteView, CountryList
from core_registration.views.state import StateCreateView, StateUpdateView, StateDeleteView, StateList
from core_registration.views.city import CityCreateView, CityUpdateView, CityDeleteView, CityList


urlpatterns = [
    #endereço, minha view.as_view()., nome da url
    path('informacao/', Informacoes_view.as_view(), name='info_core_registration'),

    path('cadastrar/company/', CompanyCreateView.as_view(), name='cadastrar_company'),
    path('editar/company/<int:pk>/', CompanyUpdateView.as_view(), name='editar_company'),
    path('listar/company/', CompanyList.as_view(), name='listar_company'),
    path('excluir/company/<int:pk>/', CompanyDeleteView.as_view(), name='excluir_company'),

    path('register/country/', CountryCreateView.as_view(), name='register_country'),
    path('edit/country/<int:pk>/', CountryUpdateView.as_view(), name='edit_country'),
    path('list/country/', CountryList.as_view(), name='list_country'),
    path('delete/country/<int:pk>/', CountryDeleteView.as_view(), name='delete_country'),

    path('register/state/', StateCreateView.as_view(), name='register_state'),
    path('edit/state/<int:pk>/', StateUpdateView.as_view(), name='edit_state'),
    path('list/state/', StateList.as_view(), name='list_state'),
    path('delete/state/<int:pk>/', StateDeleteView.as_view(), name='delete_state'),

    path('register/city/', CityCreateView.as_view(), name='register_city'),
    path('edit/city/<int:pk>/', CityUpdateView.as_view(), name='edit_city'),
    path('list/city/', CityList.as_view(), name='list_city'),
    path('delete/city/<int:pk>/', CityDeleteView.as_view(), name='delete_city'),

]