from django.contrib import admin
from mixins import SuperUserInlineAdminMixin, SuperUserAdminMixin

from .models import Address, Client


class ClientInline(SuperUserInlineAdminMixin, admin.StackedInline):
    model = Client
    extra = 1


class ClientAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number',
                    'address', 'is_active', 'company',)
    list_filter = ('is_active', 'company',)
    search_fields = ('first_name', 'last_name', 'address', 'is_active',)
    ordering = ('is_active',)


class AddressAdmin(SuperUserAdminMixin, admin.ModelAdmin):
    list_display = ('street', 'home', 'city', 'company',)
    list_filter = ('city', 'company',)
    search_fields = ('street', 'home', 'city',)
    inlines = [ClientInline,]


admin.site.register(Address, AddressAdmin)
admin.site.register(Client, ClientAdmin)
