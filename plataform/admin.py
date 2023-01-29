from django.contrib import admin
from .models import PartnerGroup, PartnerSubGroup, Partner, Category, UnMed, Item, Brand



@admin.register(PartnerGroup)
class PartnerGroupAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'group', 'company',)
    search_fields = ('group',)
    list_filter = ('company',)


@admin.register(PartnerSubGroup)
class PartnerSubGroupAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'subgroup', 'company',)
    search_fields = ('subgroup',)
    list_filter = ('company',)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nickname', 'status',)
    search_fields = ('nickname',)
    list_filter = ('company',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'category', 'markup', 'commission',)
    search_fields = ('category',)
    list_filter = ('company',)


@admin.register(UnMed)
class UnMedAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'un_med', 'description',)
    search_fields = ('un_med',)
    list_filter = ('company',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'brand', 'markup', 'commission',)
    search_fields = ('brand',)
    list_filter = ('company',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'stock_qtd', 'stock_control',)
    search_fields = ('title',)
    list_filter = ('company',)

