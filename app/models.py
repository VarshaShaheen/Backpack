from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_incorporation_certificate_number = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    financial_year = models.DateField()
    date_of_submission = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
