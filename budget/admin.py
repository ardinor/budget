from django.contrib import admin
from budget.models import Reasons, AccountTypes, Account, Transaction

# Register your models here.
admin.site.register(Reasons)
admin.site.register(AccountTypes)
admin.site.register(Account)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'type', 'amount', 'reason')
    list_filter = ['date']
    search_fields = ['reason']
    date_hierarchy = 'date'

    fieldsets = (
        (None, {'fields': ('date',)}),
        #(None, {'fields': ('account')}),
        ('Details', {'fields': ('account', ('type', 'amount', 'reason'), 'reason_other')}),
        #(None, {'fields': ('reason_other'), 'classes': ['collapse']}),  #classes adds css classes
    )

admin.site.register(Transaction, TransactionAdmin)
