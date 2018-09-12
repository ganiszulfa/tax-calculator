from django.db import models

class TaxObject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=100, blank=False)
    tax_code = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=3, default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3, default=1)

    def __str__(self):
        return self.name
