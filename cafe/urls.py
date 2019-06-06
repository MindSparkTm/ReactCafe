from django.urls import path
from .views import ListMenu,DetailMenu

urlpatterns = [
    path('menu/', ListMenu.as_view(), name='menu-all'),
    path('menu/<int:pk>',DetailMenu.as_view(),name='menu-details')
]