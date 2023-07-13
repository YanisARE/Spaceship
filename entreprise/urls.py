from django.urls import path
from .views import EntrepriseViewSet



urlpatterns = [
    path('entreprise', EntrepriseViewSet.as_view({'get': 'list'}), name='entreprise'),

]
