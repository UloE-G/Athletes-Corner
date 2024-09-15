from django.contrib import admin
from .models import Return

# Register your models here.
class ReturnAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'reasons'
    )

admin.site.register(Return, ReturnAdmin)