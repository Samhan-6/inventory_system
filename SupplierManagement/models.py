from django.db import models


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_code = models.CharField(max_length=20, unique=True)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.TextField()
    supplier_city = models.CharField(max_length=50)
    supplier_country = models.CharField(max_length=50)
    supplier_postalCode = models.CharField(max_length=10)
    supplier_addedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.supplier_name}({self.supplier_code})"
