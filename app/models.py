from django.db import models

class CompanyDetail(models.Model):
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
    client_type = models.CharField(max_length=100)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()

    def __str__(self):
        return self.company_name_en

class CorporateDocument(models.Model):
    company = models.ForeignKey(CompanyDetail, on_delete=models.CASCADE, related_name='documents')
    document_file = models.FileField(upload_to='corporate_documents/')
    document_name = models.CharField(max_length=255)
    document_number = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    department_portal = models.CharField(max_length=255)
    portal_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.document_name} ({self.document_number})"

