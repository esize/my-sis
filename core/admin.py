from django.contrib import admin
from .models import Person, Address, AddressType, PhoneNumber, PhoneNumberType, Name
# Inline admin for Address
class AddressInline(admin.StackedInline):
    model = Address
    extra = 1  # Number of empty forms to display initially

# Inline admin for PhoneNumber
class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 1  # Number of empty forms to display initially

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'personal_email', 'active')
    search_fields = ('first_name', 'last_name', 'personal_email')
    inlines = [AddressInline, PhoneNumberInline]

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'active')
    search_fields = ('first_name', 'last_name')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state_province', 'postal_code', 'country', 'address_type', 'active')
    search_fields = ('street_address', 'city', 'state_province', 'postal_code', 'country')
    readonly_fields = ('street_address', 'city', 'state_province', 'postal_code', 'country', 'address_type', 'active')

@admin.register(AddressType)
class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'phone_type', 'is_primary', 'active')
    search_fields = ('number',)
    readonly_fields = ('number', 'phone_type', 'is_primary', 'active')

@admin.register(PhoneNumberType)
class PhoneNumberTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    search_fields = ('name',)