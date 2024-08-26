from core.models import BaseModel
from django.db import models
from auditlog.registry import auditlog
from django.core.exceptions import ValidationError

class GradingBasis(BaseModel):
    """
    Grading basis (ex: Letter, pass/fail, audit, etc.)
    """
    name = models.CharField(max_length=255)
    impacts_gpa = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Grading Basis'
        verbose_name_plural = 'Grading Bases'
auditlog.register(GradingBasis)

class GradingBasisValue(BaseModel):
    """
    Grading basis value (ex: A, B, C, D, F, etc.)
    """
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)
    basis = models.ForeignKey(GradingBasis, on_delete=models.CASCADE, related_name='values')
    gpa_value = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        if self.basis.impacts_gpa and (self.gpa_value is not None and (self.gpa_value < 0 or self.gpa_value > 4)):
            raise ValidationError('GPA value must be between 0 and 4')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Grading Basis Value'
        verbose_name_plural = 'Grading Basis Values'
auditlog.register(GradingBasisValue)