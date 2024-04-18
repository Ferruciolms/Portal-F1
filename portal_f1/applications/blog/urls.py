from django.urls import path
from blog.views.index import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='blog'),
]
