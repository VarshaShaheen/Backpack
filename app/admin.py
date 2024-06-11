from django.contrib import admin
from .models import CompanyDetail


class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = [
        'company_name_en', 'company_name_ar', 'email', 'mobile', 'website',
        'national_address', 'po_box_no', 'city', 'country', 'contact_person_name',
        'title', 'contact_person_mobile', 'fiscal_year_end', 'due_date_of_tax_fs_submission',
        'vat_submission_period', 'latest_vat_filed', 'client_type', 'contract_start_date', 'contract_end_date'
    ]
    search_fields = ['company_name_en', 'company_name_ar', 'city', 'country', 'contact_person_name']
    list_filter = ['city', 'country', 'client_type', 'fiscal_year_end', 'due_date_of_tax_fs_submission']


admin.site.register(CompanyDetail, CompanyDetailAdmin)
