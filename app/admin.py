from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'phone_number', 'company_incorporation_certificate_number', 'issue_date',
                    'expiry_date', 'financial_year', 'date_of_submission']
    search_fields = ['company_incorporation_certificate_number','company_name']