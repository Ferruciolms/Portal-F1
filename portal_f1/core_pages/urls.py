from django.urls import path
from core_pages.views.index import IndexSystemView



urlpatterns = [
    #endereço, minha view.as_view()., nome da url
    path('inicio', IndexSystemView.as_view(), name='inicio'),
    # path('equipenocs/', EquipeView.as_view(), name='equipe'),
]
