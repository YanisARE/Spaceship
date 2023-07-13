from django.urls import path
from .views import ModuleViewSet

module_list = ModuleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

module_detail = ModuleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('module', ModuleViewSet.as_view({'get': 'list'}), name='module'),

]
