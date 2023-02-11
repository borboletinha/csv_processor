from django.contrib import admin

from deals.models import Deal


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    fields = ('customer', 'item', 'quantity', 'price', 'deal_date')
    readonly_fields = ('deal_date',)
