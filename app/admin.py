from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import CompanyDetail, CorporateDocument

class BackPackAdminSite(AdminSite):
    site_header = 'BackPack Administration'
    site_title = 'BackPack Admin'
    index_title = 'BackPack Site Administration'

admin_site = BackPackAdminSite(name='backpack')

class CorporateDocumentInline(admin.TabularInline):
    model = CorporateDocument
    extra = 1
    fields = [
        'document_file', 'document_name', 'document_number', 'issue_date',
        'expiry_date', 'department_portal', 'portal_access'
    ]

class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = [
        'company_name_en', 'company_name_ar', 'email', 'telephone', 'mobile',
        'website', 'national_address', 'po_box_no', 'city', 'country',
        'contact_person_name', 'title', 'contact_person_mobile', 'contact_person_email',
        'fiscal_year_end', 'due_date_of_tax_fs_submission', 'vat_submission_period',
        'latest_vat_filed', 'client_type', 'contract_start_date', 'contract_end_date'
    ]
    search_fields = [
        'company_name_en', 'company_name_ar', 'email', 'city', 'country',
        'contact_person_name', 'contact_person_email'
    ]
    list_filter = [
        'city', 'country', 'client_type', 'fiscal_year_end', 'due_date_of_tax_fs_submission',
        'vat_submission_period'
    ]
    inlines = [CorporateDocumentInline]

# Register the admin class with the new admin site
admin_site.register(CompanyDetail, CompanyDetailAdmin)
