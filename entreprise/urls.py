from django.urls import path
from .views import EntrepriseViewSet

entreprise_list = EntrepriseViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

entreprise_detail = EntrepriseViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('entreprise/', entreprise_list, name='entreprise-list'),
    path('entreprise/<int:pk>/', entreprise_detail, name='entreprise-detail'),
]
