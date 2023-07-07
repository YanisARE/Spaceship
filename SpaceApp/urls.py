from django.urls import include, path
from rest_framework.routers import DefaultRouter
from orbiteur.views import OrbiteurViewSet
from module.views import ModuleViewSet
from pays.views import PaysViewSet
from entreprise.views import EntrepriseViewSet
from django.contrib import admin

router = DefaultRouter()
router.register(r'pays', PaysViewSet)
router.register(r'orbiteurs', OrbiteurViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'entreprises', EntrepriseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
