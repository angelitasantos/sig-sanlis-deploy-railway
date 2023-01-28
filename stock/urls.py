from django.urls import path, include
from . import views as v


app_name = 'stock'


sale_patterns = [
    path('', v.stock_sale_list, name='stock_sale_list'),
    path('<int:pk>/', v.stock_sale_detail, name='stock_sale_detail'),
    path('add/', v.stock_sale_add, name='stock_sale_add'),
]

service_patterns = [
    path('', v.stock_service_list, name='stock_service_list'),
    path('<int:pk>/', v.stock_service_detail, name='stock_service_detail'),
    path('add/', v.stock_service_add, name='stock_service_add'),
]

shopping_patterns = [
    path('', v.stock_shopping_list, name='stock_shopping_list'),
    path('<int:pk>/', v.stock_shopping_detail, name='stock_shopping_detail'),
    path('add/', v.stock_shopping_add, name='stock_shopping_add'),
]

production_patterns = [
    path('', v.stock_production_list, name='stock_production_list'),
    path('<int:pk>/', v.stock_production_detail, name='stock_production_detail'),
    path('add/', v.stock_production_add, name='stock_production_add'),
]

inventary_patterns = [
    path('', v.stock_inventary_list, name='stock_inventary_list'),
    path('<int:pk>/', v.stock_inventary_detail, name='stock_inventary_detail'),
    path('add/', v.stock_inventary_add, name='stock_inventary_add'),
]


urlpatterns = [
    path('vendas/', include(sale_patterns)),
    path('servicos/', include(service_patterns)),
    path('compras/', include(shopping_patterns)),
    path('producao/', include(production_patterns)),
    path('inventario/', include(inventary_patterns)),
]
