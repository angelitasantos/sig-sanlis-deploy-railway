from django.urls import path, include
from . import views

app_name = 'plataform'


partners_patterns = [
    path('', views.partners, name='partners'),
    path('novo_parceiro/', views.partner_create, name='partner_create'),
    path('visualizar_parceiro/<int:id>', views.partner_view, name="partner_view"),
    path('alterar_parceiro/<int:id>', views.partner_update, name="partner_update"),
    path('excluir_parceiro/<int:id>', views.partner_delete, name="partner_delete"),
]

items_patterns = [
    path('', views.items, name='items'),
    path('novo_item/', views.item_create, name='item_create'),
    path('visualizar_item/<int:id>', views.item_view, name="item_view"),
    path('alterar_item/<int:id>', views.item_update, name="item_update"),
    path('excluir_item/<int:id>', views.item_delete, name="item_delete"),
    
    # Ajax para Saldo
    path('<int:pk>/json/', views.produto_json, name='produto_json'),

    path('nova_un_med/', views.un_med_create, name='un_med_create'),
    path('nova_categoria/', views.category_create, name='category_create'),
]

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('parceiros/', include(partners_patterns)),
    path('itens/', include(items_patterns)),
]
