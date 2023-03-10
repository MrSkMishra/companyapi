from django.contrib import admin
from apiapp.models import Company,Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','location','type')
    search_fields=('name','location')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','position','company')
    list_filter=['company']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

