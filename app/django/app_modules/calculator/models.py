from django.db import models

class TaxObject(models.Model):
    name = models.CharField(max_length=100, blank=False)
    tax_code = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)
    tax_amount = models.DecimalField(blank=True,max_digits=10, decimal_places=3, default=1)
    total_amount = models.DecimalField(blank=True,max_digits=10, decimal_places=3, default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.tax_code == 1:
            self.tax_amount = 0.1 * self.amount
        elif self.tax_code == 2:
            self.tax_amount = 10 + 0.02 * self.amount
        elif self.tax_code == 3:
            if self.amount < 100:
                self.tax_amount = 0
            else:
                self.tax_amount = 0.01 * (self.amount-100)
        else:
            return False
        self.total_amount = self.amount + self.tax_amount
        super(TaxObject, self).save(*args, **kwargs)
