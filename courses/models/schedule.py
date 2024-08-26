from core.models import BaseModel
from django.db import models
from auditlog.registry import auditlog
from django.core.exceptions import ValidationError

class CourseMeetingDays(BaseModel):
    code = models.CharField(max_length=255)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    def clean(self):
        if not any(
            (
                self.monday,
                self.tuesday,
                self.wednesday,
                self.thursday,
                self.friday,
                self.saturday,
                self.sunday,
            )
        ):
            raise ValidationError("Course meeting pattern must contain at least one day of the week")
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = 'Course Meeting Pattern Days'
        verbose_name_plural = 'Course Meeting Pattern Days'

auditlog.register(CourseMeetingDays)

class CourseMeetingPeriod(BaseModel):
    code = models.CharField(max_length=255)
    start_time = models.TimeField()
auditlog.register(CourseMeetingPeriod)

class CourseMeetingPattern(BaseModel):
    code = models.CharField(max_length=255)
    days = models.ForeignKey(CourseMeetingDays, on_delete=models.CASCADE)
    time = models.ForeignKey(CourseMeetingPeriod, on_delete=models.CASCADE)
    sort_order = models.IntegerField()
    recurring_every_number_of_weeks = models.IntegerField(default=1)

    def __str__(self):
        return self.code

auditlog.register(CourseMeetingPattern)