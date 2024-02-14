from django.urls import path
from . import views

urlpatterns = [
    # path('', views.transfer_data),
    path('create_category/', views.add_category, name="create_category"),
    path('deactivate_category/<int:id>', views.deactivate_category, name="deactivate_category"),
    path('activate_category/<int:id>', views.activate_category, name="activate_category"),
    path('delete_category/<int:id>', views.delete_category, name="delete_category"),
    path('vehicles_entry/', views.vehicles_entry, name="vehicles_entry"),
    path('manage_vehicles/', views.manage_vehicles, name="manage_vehicles"),
    path('action/<int:id>', views.changing_status_based_on_action, name="action"),
    path('search/', views.search, name="search"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('change_password/', views.change_password, name="change_passwords"),
    path('logout/', views.logouts, name="logout"),
    path('shyam/', views.base, name="user"),
    path('edit/<int:id>', views.editss, name="edit"),

]