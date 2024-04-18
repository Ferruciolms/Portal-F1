"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views


schema_view = get_schema_view(
   openapi.Info(
      title="Instituto Nacional da Mata Atlântica",
      default_version='v1',
      description="Instituto Nacional da Mata Atlântica",
      # terms_of_service="https://www.google.com/policies/terms/",
      # contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_pages.urls')),
    path('', include('core_access.urls')),
    path('', include('core_registration.urls')),
    path('', include('analytics.urls')),
    path('', include('blog.urls')),


    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
