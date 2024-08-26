from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel

class AcademicLevel(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Academic Level'
        verbose_name_plural = 'Academic Levels'

auditlog.register(AcademicLevel)