from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('activation.urls')),
    path('', include('home.urls')),
    path('painel/', include('plataform.urls')),
    path('painel/estoque/', include('stock.urls')),
]
