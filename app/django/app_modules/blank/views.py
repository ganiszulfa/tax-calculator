# PYTHON LIBRARY
import logging


# DJANGO LIBRARY
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

# THIRD-PARTY LIBRARY


# app_core LIBRARY
from app_core.common import base_decode, base_encode

# Get an instance of a logger
logger = logging.getLogger(__name__)

def index(request):
    """docstring for index"""
    return HttpResponse("hello too")
    
