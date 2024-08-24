from django.db import models
from auditlog.registry import auditlog

from .address import Address
from .base import BaseModel
from .name import Name
from .phone_number import PhoneNumber


class Person(BaseModel):
    legal_name=models.ForeignKey(Name, on_delete=models.CASCADE, related_name='person_legal_name')
    preferred_name=models.ForeignKey(Name, on_delete=models.CASCADE, related_name='person_preferred_name', null=True, blank=True)
    personal_email=models.EmailField(unique=True, blank=True, null=True)
    date_of_birth=models.DateField(null=True, blank=True)


    def full_name(self):
        if self.preferred_name:
            return self.preferred_name.full_name()
        return self.legal_name.full_name()
    
    def friendly_name(self):
        if self.preferred_name:
            return self.preferred_name.first_name
        return self.legal_name.first_name
    
    def __str__(self):
        return f"{self.full_name()}"

auditlog.register(Person)