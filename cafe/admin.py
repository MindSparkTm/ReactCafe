from django.contrib import admin
# Register your models here.
from .models import Menu

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name','type','currency','date_added')
    readonly_fields = ('date_added', 'date_last_modified')
    ordering = ['date_last_modified']
admin.site.register(Menu,MenuItemAdmin)