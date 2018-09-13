from django.test import TestCase
from .models import TaxObject

class TaxObjectTestCase(TestCase):
    def setUp(self):
        TaxObject.objects.create(name="cigs", tax_code=2, amount=1000)
        TaxObject.objects.create(name="food", tax_code=1, amount=1000)
        TaxObject.objects.create(name="movie", tax_code=3, amount=150)
        TaxObject.objects.create(name="invalid", tax_code=4, amount=100)

    def test_tax_amount(self):
        cigs = TaxObject.objects.get(name="cigs")
        self.assertEqual(cigs.tax_amount, 30.0)
        food = TaxObject.objects.get(name="food")
        self.assertEqual(food.tax_amount, 100.0)
        movie = TaxObject.objects.get(name="movie")
        self.assertEqual(movie.tax_amount, 0.5)

    def test_invalid_tax_code(self):
        invalid = None
        try:
            invalid = TaxObject.objects.get(name="invalid")
        except:
            pass
        self.assertIsNone(invalid)
