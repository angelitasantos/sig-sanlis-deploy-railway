from django.contrib import admin
from .models import Company, TokenUser



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'full_name', 'phone', 'token_company', 'user_company',)
    search_fields = ('name',)
    list_filter = ('user_company',)


@admin.register(TokenUser)
class TokenUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active', 'company', 'token', )
    search_fields = ('user',)
    list_filter = ('company',)
