from django.db import models
from auditlog.registry import auditlog

from core.utils import normalize_phone_number

from .base import BaseModel


class PhoneNumberType(BaseModel):
    name = models.CharField(max_length=25, unique=True)
    sms = models.BooleanField()

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Phone Number Type'
        verbose_name_plural = 'Phone Number Types'

auditlog.register(PhoneNumberType)

class PhoneNumber(BaseModel):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='phone_numbers', null=True, blank=True)
    number = models.CharField(max_length=20)
    phone_type = models.ForeignKey(PhoneNumberType, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.number = normalize_phone_number(self.number)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} ({self.phone_type})"
auditlog.register(PhoneNumber)