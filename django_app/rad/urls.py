from django.urls import path

from . import views

# Adds all the URLs so they can be navigated to

urlpatterns = [
    path('', views.index, name='index'),
    path('traders/', views.traders, name='traders'),
    path('distros/', views.distros, name='distros'),
    path('trader_distros/', views.traderDistro, name='trader_distros'),
    path('distros_display/', views.distroDisplay, name='distros_display'),

    path('trader/add', views.traderRequest, name='add_trader'),
    path('distros/add', views.distroRequest, name='add_distro'),
    path('trader_distros/add', views.traderDistroRequest, name='add_trader_distro'),
    path('distro_change_state_request/', views.distroChangeStateRequest, name='distro_change_state_request'),
]
