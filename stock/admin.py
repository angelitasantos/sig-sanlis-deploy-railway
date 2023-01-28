from django.contrib import admin
from .models import ( 
                        Estoque,
                        StockSale,
                        StockService,
                        StockShopping,
                        StockProduction,
                        StockInventary,
                        EstoqueItens
                    )


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(Estoque)
class StockAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario', 'company_id')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(StockSale)
class StockSaleAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario', 'company_id')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(StockService)
class StockServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(StockShopping)
class StockShoppingAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(StockProduction)
class StockProductionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(StockInventary)
class StockInventaryAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
