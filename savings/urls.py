from django.urls import path
from . import views

urlpatterns = [
    path('', views.saving_goals_list, name='saving_goals_list'),
    path('add/', views.add_saving_goal, name='add_saving_goal'),
    path('edit/<int:pk>/', views.edit_saving_goal, name='edit_saving_goal'),
    path('delete/<int:pk>/', views.delete_saving_goal, name='delete_saving_goal'),
    path('deposit/<int:pk>/', views.deposit_to_saving_goal, name='deposit_to_saving_goal'), 
]
