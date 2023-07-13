from django.urls import path
from .views import OrbiteurViewSet

urlpatterns = [
    path('orbiteur', OrbiteurViewSet.as_view({'get': 'list'}), name='orbiteur'),

]
