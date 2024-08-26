from core.models import BaseModel
from django.core.exceptions import ValidationError
from django.db import models
from auditlog.registry import auditlog

class AcademicUnitType(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Academic Unit Type'
        verbose_name_plural = 'Academic Unit Types'

auditlog.register(AcademicUnitType)

class AcademicUnit(BaseModel):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=16, blank=True, null=True)
    unit_type = models.ForeignKey(AcademicUnitType, on_delete=models.SET_NULL, null=True, related_name='academic_units')
    description = models.TextField(blank=True, null=True)
    academic_levels = models.ManyToManyField('AcademicLevel', related_name='academic_units')
    superior_unit = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subordinate_units', null=True, blank=True)
    is_institution = models.BooleanField(default=False)
    attributes = models.JSONField(blank=True, null=True, default=dict)

    def __str__(self):
        return self.name
    
    def clean(self):
        # If this unit is marked as an institution, it must not have a superior unit
        if self.is_institution and self.superior_unit is not None:
            raise ValidationError('An institution cannot have a superior unit')
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Academic Unit'
        verbose_name_plural = 'Academic Units'

auditlog.register(AcademicUnit)