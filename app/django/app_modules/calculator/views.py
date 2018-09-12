# PYTHON LIBRARY
import logging


# DJANGO LIBRARY
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

# THIRD-PARTY LIBRARY


# app_core LIBRARY
from app_core.common import base_decode, base_encode
from .forms import TaxForm
from .models import TaxObject

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            tax_code = form.cleaned_data['tax_code']
            amount = form.cleaned_data['amount']
            if tax_code == 1:
                tax_amount = 0.1 * amount
            elif tax_code == 2:
                tax_amount = 10 + 0.02 * amount
            elif tax_code == 3:
                if amount < 100:
                    tax_amount = 0
                else:
                    tax_amount = 0.01 * (amount-100)
            total_amount = amount + tax_amount
            TaxObject(name=name, tax_code=tax_code, amount=amount,
                    tax_amount=tax_amount, total_amount=total_amount).save()

            return HttpResponseRedirect(reverse('view_my_bill', ))
    else:
        form = TaxForm()

    return render(request, 'add_tax_object.html', {'form': form})

def view_my_bill(request):
    tax_objects = TaxObject.objects.all()
    total_tax = 0
    total_amount = 0
    grand_amount = 0
    for t in tax_objects:
        total_tax += t.tax_amount
        total_amount += t.amount
        grand_amount += t.total_amount

    return render(request, 'view_my_bill.html', {
        'tax_objects': tax_objects,
        'total_tax': total_tax,
        'total_amount': total_amount,
        'grand_amount': grand_amount,
        })
