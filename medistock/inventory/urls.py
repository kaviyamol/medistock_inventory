from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('medicine_list/', views.medicine_list, name='medicine_list'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('delete/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('remove-expired/', views.remove_expired, name='remove_expired'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome, name='welcome'),
    path('help/', views.help_view, name='help'),
]
