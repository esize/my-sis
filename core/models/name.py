from django.db import models

from core.models import BaseModel

from auditlog.registry import auditlog

class Name(BaseModel):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def formal_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
auditlog.register(Name)