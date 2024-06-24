from django.db import models


class CompanyDetail(models.Model):
    CLIENT_TYPES = (
        ('citco_gsgs', 'Citco GSGS'),
        ('package_annual_maintenance', 'Package Annual Maintenance'),
        ('contract_amc_regular_client', 'Contract AMC Regular Client'),
    )

    company_name_en = models.CharField(max_length=255)
    company_name_ar = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    national_address = models.CharField(max_length=255)
    po_box_no = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    contact_person_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    contact_person_mobile = models.CharField(max_length=20)
    contact_person_email = models.EmailField()
    fiscal_year_end = models.DateField()
    due_date_of_tax_fs_submission = models.DateField()
    vat_submission_period = models.CharField(max_length=100)
    latest_vat_filed = models.DateField()
    client_type = models.CharField(max_length=100, choices=CLIENT_TYPES)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()

    def __str__(self):
        return self.company_name_en


class CorporateDocument(models.Model):
    PORTAL_ACCESS_CHOICES = (
        ('misa', 'Ministry of investment MISA License'),
        ('commercial_registration', 'Commercial Registration'),
        ('company_unified_no', 'Company Unified NO:'),
        ('chamber_of_commerce', 'Chamber of Commerce'),
        ('ministry_of_labor', 'Ministry of Labor'),
        ('social_insurance_gosi', 'Social Insurance GOSI'),
        ('qiwa', 'Qiwa'),
        ('mudad', 'Mudad'),
        ('muqeem', 'Muqeem'),
        ('zackat_tax_certificate', 'Zackat/Tax Certificate'),
        ('vat_registration', 'Value Added Tax Registration VAT'),
        ('saudipost', 'Saudipost (National Address)'),
        ('tamm', 'Tamm'),
        ('abshir', 'Abshir for General Manager/Director'),
        ('municipality_license', 'Municipality License Baladiya'),
        ('ministry_of_tourism', 'Ministry of Tourism'),
    )

    company = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='documents')
    document_file = models.FileField(upload_to='corporate_documents/')
    document_name = models.CharField(max_length=100, choices=PORTAL_ACCESS_CHOICES, blank=True, null=True)
    document_number = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    department_portal = models.CharField(max_length=255)
    portal_access = models.CharField(max_length=255)
    username = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    otp_mobile = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.document_name} ({self.document_number})"
