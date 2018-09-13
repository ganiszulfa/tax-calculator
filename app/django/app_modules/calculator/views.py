# PYTHON LIBRARY
import logging


# DJANGO LIBRARY
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# THIRD-PARTY LIBRARY
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# app_core LIBRARY
from app_core.common import base_decode, base_encode
from .forms import TaxForm
from .models import TaxObject
from .serializers import TaxObjectSerializer

logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            tax_code = form.cleaned_data['tax_code']
            amount = form.cleaned_data['amount']
            TaxObject(name=name, tax_code=tax_code, amount=amount).save()

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

@csrf_exempt
def tax_object_list(request):
    """
    List all code tax_objects, or create a new tax_object.
    """
    if request.method == 'GET':
        tax_objects = TaxObject.objects.all()
        serializer = TaxObjectSerializer(tax_objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaxObjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tax_object_detail(request, pk):
    """
    Retrieve, update or delete a tax_object.
    """
    try:
        tax_object = TaxObject.objects.get(pk=pk)
    except TaxObject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TaxObjectSerializer(tax_object)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaxObjectSerializer(tax_object, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        tax_object.delete()
        return HttpResponse(status=204)
