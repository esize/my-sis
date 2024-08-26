from core.models import BaseModel
from django.db import models
from auditlog.registry import auditlog
from django.core.exceptions import ValidationError
from .schedule import CourseMeetingPattern
from academic_structure.models import AcademicPeriod, Location

class CourseSectionType(BaseModel):
    """
    Course section type (ex: Lecture, Lab, etc.)
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

auditlog.register(CourseSectionType)

class CourseSection(BaseModel):
    """
    Course section (ex: 001, 002, etc.)
    """
    code = models.CharField(max_length=8)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    academic_period = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE)
    tags = models.ManyToManyField('CourseTag', related_name='course_sections')
    hidden = models.BooleanField(default=False)
    status = models.CharField(max_length=255, choices=[ ('preliminary', 'preliminary'), ('open', 'open'), ('waitlist', 'waitlist'), ('hold', 'hold'), ('closed', 'closed'), ('cancelled', 'cancelled')], default='preliminary')
    """
    - preliminary - When you first create a course section.
    - open - When you publish a course section, making it available for student registration.
    - waitlist - When a published course section reaches its capacity and the waitlist opens
    - hold - When the published course section is in the process of cancellation. This status indicates that the course section is awaiting approval in the Student Course Section Cancel Event business process.
    - closed - When a published course section reaches:
                - Section capacity and there's no waitlist.
                - Waitlist capacity.
    - cancelled - When the Student Course Section Cancel Event business process completes.
    """
    

    bookstore_url = models.URLField(blank=True, null=True)
    meeting_pattern = models.ForeignKey(CourseMeetingPattern, on_delete=models.SET_NULL, null=True, blank=True)
    section_type = models.ForeignKey(CourseSectionType, on_delete=models.SET_NULL, null=True, blank=True)
    delivery_mode = models.CharField(max_length=255, choices=[('In-Person', 'In-Person'), ('Online', 'Online'), ('Hybrid', 'Hybrid')])
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True) # Anything from a Room in a building to a campus

    def clean(self):
        if self.location.usage not in ['Instructional', 'Campus']:
            raise ValidationError('A course section must be assigned to a location utilized as instructional or a campus.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Course Section'
        verbose_name_plural = 'Course Sections'

    def __str__(self):
        return self.name
auditlog.register(CourseSection)