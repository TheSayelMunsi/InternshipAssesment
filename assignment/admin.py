from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(client_table)
admin.site.register(Artist_table)
admin.site.register(Work_table)