from core.models import BaseModel
from django.db import models
from auditlog.registry import auditlog
from core.models import Address
from academic_structure.models import AcademicUnit

class LocationAttributes(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name
    
class LocationAttributeMapping(BaseModel):
    attribute = models.ForeignKey(LocationAttributes, on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Location(BaseModel):
    name = models.CharField(max_length=255)
    usage = models.CharField(max_length=255, choices=[('Campus', 'Campus'), ('Instructional', 'Instructional'), ('Housing', 'Housing')], default='Instructional')
    owning_unit = models.ForeignKey(AcademicUnit, on_delete=models.CASCADE, null=True, blank=True)
    superior_location = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinate_locations')
    capacity = models.IntegerField(null=True, blank=True)
    instructional_use_only = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'