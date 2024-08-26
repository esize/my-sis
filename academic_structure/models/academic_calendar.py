from core.models import BaseModel
from django.db import models
from auditlog.registry import auditlog

class AcademicCalendar(BaseModel):
    """
    Academic Calendar (ex: Semester Calendar, Quarter Calendar, etc.)
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
auditlog.register(AcademicCalendar)
    
class AcademicYear(BaseModel):
    """
    Academic year (ex: 2020-2021, 2021-2022, etc.)
    """
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    calendar = models.ForeignKey(AcademicCalendar, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

auditlog.register(AcademicYear)

class AcademicPeriodType(BaseModel):
    """
    Academic period type (ex: Spring, Fall, and Intersession)
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

auditlog.register(AcademicPeriodType)

class AcademicPeriod(BaseModel):
    """
    Academic period (ex: Fall 2020, Spring 2021, etc.)
    """
    period_type = models.ForeignKey(AcademicPeriodType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

auditlog.register(AcademicPeriod)