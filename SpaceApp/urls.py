from django.urls import include, path
from rest_framework.routers import DefaultRouter
from orbiteur.views import OrbiteurViewSet
from module.views import ModuleViewSet
from pays.views import PaysViewSet
from entreprise.views import EntrepriseViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'pays', PaysViewSet)
router.register(r'orbiteur', OrbiteurViewSet) # J'ai changé car il y avait un s en trop
router.register(r'module', ModuleViewSet)  # Pareil
router.register(r'entreprise', EntrepriseViewSet) # Pareil

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('orbiteur/update_all_coordinates/', OrbiteurViewSet.as_view({'post': 'update_all_coordinates'})),
]
