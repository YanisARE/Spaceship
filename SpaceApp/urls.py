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

router = DefaultRouter()
router.register(r'pays', PaysViewSet)
router.register(r'orbiteur', OrbiteurViewSet)  # J'ai changé, car il y avait un s en trop
router.register(r'module', ModuleViewSet)  # Pareil
router.register(r'entreprise', EntrepriseViewSet)  # Pareil

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('orbiteur/update_all_coordinates/', OrbiteurViewSet.as_view({'post': 'update_all_coordinates'})),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
