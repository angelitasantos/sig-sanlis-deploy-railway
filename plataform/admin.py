from django.contrib import admin
from .models import PartnerGroup, PartnerSubGroup, Partner, Category, UnMed, Item, Brand


admin.site.register(PartnerGroup)
admin.site.register(PartnerSubGroup)
admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(UnMed)
admin.site.register(Brand)
admin.site.register(Item)
