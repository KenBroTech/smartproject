from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('addmeter/', views.add_meter, name='dashboard-addmeter'),
    path('detail/<int:pk>/', views.detail, name='dashboard-detail'),
]
