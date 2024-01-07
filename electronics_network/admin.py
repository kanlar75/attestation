from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronics_network.models import Contact
from electronics_network.models import Company
from electronics_network.models import Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'company', 'country', 'city',)
    list_filter = ('country',)
    list_display_links = ('company',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'model', 'get_company',)
    list_filter = ('company',)
    list_display_links = ('pk', 'name', 'get_company',)

    @admin.display(description="Компания")
    def get_company(self, obj):
        contacts = obj.company
        if contacts:
            url = reverse('admin:electronics_network_contact_change',
                          args=[contacts.id])
            return format_html('<a href="{}">{}</a>', url, contacts)
        return '---'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'get_supplier', 'debt',)
    list_filter = ('contacts__country',)
    actions = ('clear_the_debt',)
    list_display_links = ('pk', 'get_supplier', 'name')
    list_editable = ('debt',)

    @admin.display(description="Поставщик")
    def get_supplier(self, obj):
        supplier = obj.supplier

        if supplier:
            url = reverse('admin:electronics_network_company_change',
                          args=[supplier.id])
            return format_html('<a href="{}">{}</a>', url, supplier)
        return '---'

    @admin.action(description='Удалить задолженность')
    def clear_the_debt(self, request, queryset):
        queryset.update(debt=0.00)
        self.message_user(request, "Задолженность удалена.")
