from django.urls import path
from .views import (
    addPipeView,pipelistView, 
    deletePipeView, 
    updatePipeView, 
    contentslistView, 
    coatinglistView,
    detailsView
)

urlpatterns = [
    path('add-pipe/', addPipeView, name='add-pipe'),
    path('pipe-list/', pipelistView, name='pipe-list'),
    path('delete-pipe/<int:id>/', deletePipeView, name='delete-pipe'),
    path('update-pipe/<int:id>/', updatePipeView, name='update-pipe'),

    path('content-list/', contentslistView, name='content-list'),
    path('coating-list/', coatinglistView, name='coating-list'),
    path('details/<int:id>/',detailsView,name='details')
]
