from django.contrib import admin
from first import models
# Register your models here.
admin.site.register(models.c)
admin.site.register(models.usd_to_currency)
admin.site.register(models.dec_currency)
