from django.urls import path
from .views import PaysViewSet



urlpatterns = [
    path('pays', PaysViewSet.as_view({'get': 'list'}), name='pays'),

]
