from django.contrib import admin

# Register your models here.
from .models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'total', 'quantity', 'date')
