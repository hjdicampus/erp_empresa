from django.contrib import admin
from django.urls import path
from coremp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('comprar/', views.comprar, name='comprar'),
    path('publico_registrado/', views.publico_registrado, name='publico_registrado'),
    path('pago/<int:plan_id>/', views.pago, name='pago'),
]

