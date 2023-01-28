from django.contrib import admin
from .models import Company, TokenUser


admin.site.register(TokenUser)
admin.site.register(Company)
