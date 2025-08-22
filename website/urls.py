from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),
    path('create/', views.create, name = 'create'),
    path('record/<int:pk>', views.customerRecord, name = 'record'),
    path('delete/<int:pk>', views.deleteRecord, name = 'delete'),
    path('modify/<int:pk>', views.modifyRecord, name = 'modify'),

]