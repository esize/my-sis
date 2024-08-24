from django.db import models

from .base import BaseModel
from auditlog.registry import auditlog

class AddressType(BaseModel):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Address Type'
        verbose_name_plural = 'Address Types'
auditlog.register(AddressType)

class Address(BaseModel):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='addresses', null=True, blank=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=100, blank=True)
    address_type = models.ForeignKey(AddressType, on_delete=models.CASCADE)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

auditlog.register(Address)