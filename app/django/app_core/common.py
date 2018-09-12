import random
import datetime
import logging
import time
import pytz
import json

import django

from django.conf import settings
from django.core.cache import cache
from django.contrib import admin

# Get an instance of a logger
logger = logging.getLogger(__name__)

BASE_ALPH = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)
BIGINT_BIT = 64
ONE_MONTH = 30 * 24 * 3600

def timestamp_to_dt_tz(timestamp):
    local_tz = pytz.timezone(settings.TIME_ZONE) 
    utc_dt = datetime.datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
    return local_tz.normalize(utc_dt.astimezone(local_tz))

def dt_to_timestamp(dt):
    return round(time.mktime(dt.timetuple()))

def dt_to_tz_aware(dt):
    return pytz.timezone(settings.TIME_ZONE).localize(dt)

def get_safe_token(i):
    return base_encode(random.getrandbits(i))

def base_decode(string):
    num = 0
    for char in string:
        num = num * BASE_LEN + BASE_DICT[char]
    return num

def base_encode(num):
    if not num:
        return BASE_ALPH[0]

    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[rem] + encoding
    return encoding


class CommonModelAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        display_hidden_fields = [ "id",]
        filter_hidden_fields = list(display_hidden_fields)
        filter_hidden_fields.extend([ "token", ])
        self.list_display = [field.name for field in model._meta.fields if field.name not in display_hidden_fields]
        self.list_filter = [field.name for field in model._meta.fields if field.name not in filter_hidden_fields]

        super(CommonModelAdmin, self).__init__(model, admin_site)

def dict_to_json_obj(d):
    return json.loads( json.dumps(d) )
