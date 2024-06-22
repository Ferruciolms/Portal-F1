from django.urls import path
from blog.views.index import IndexView, GalleryView, CircuitView, ContactView



urlpatterns = [
    path('', IndexView.as_view(), name='blog'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('circuits/', CircuitView.as_view(), name='circuits'),
    path('contact/', ContactView.as_view(), name='contact'),
]
