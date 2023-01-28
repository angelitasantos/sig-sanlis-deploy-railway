from django.urls import path
from . import views


app_name = 'activation'

urlpatterns = [
    path('registrar/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('sair/', views.logout, name='logout'),
    path('ativar_conta/<str:token>/', views.active_account, name="active_account"),

    path('empresas/', views.companies, name='companies'),
    path('nova_empresa/', views.company_create, name='company_create'),
    path('visualizar_empresa/<int:id>', views.company_view, name="company_view"),
    path('alterar_empresa/<int:id>', views.company_update, name="company_update"),
    path('excluir_empresa/<int:id>', views.company_delete, name="company_delete"),
]
