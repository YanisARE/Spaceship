from django.shortcuts import redirect
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from orbiteur.views import OrbiteurViewSet
from module.views import ModuleViewSet
from pays.views import PaysViewSet
from entreprise.views import EntrepriseViewSet
from django.contrib import admin
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Spaceship API",
        default_version='v1',
        description="API Spaceship, projet de stage",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@Spaceship.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Définit une vue de redirection pour l'URL racine ("/") pour rediriger vers l'application "orbiteur"
def redirect_to_orbiteur(request):
    return redirect('orbiteur')  # Remplace "orbiteur-list" par le nom d'URL approprié pour l'application
    # "orbiteur"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('orbiteur/update_all_coordinates/', OrbiteurViewSet.as_view({'post': 'update_all_coordinates'})),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), # generate interactive API documentation
    path('api/', include('orbiteur.urls')),
    path('api/', include('module.urls')),
    path('api/', include('entreprise.urls')),
    path('api/', include('pays.urls')),
    path('', redirect_to_orbiteur),  # line to redirect the root URL ("/") to the "orbiteur" app
]
