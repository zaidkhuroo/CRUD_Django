from django.urls import path
from . import views
urlpatterns = [

    path('',views.index,name=''),
    path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('add_record', views.add_record,name='add_record'),
]
