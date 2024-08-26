from academic_structure.models.academic_unit import AcademicUnit
from core.models import BaseModel
from academic_structure.models import Location
from django.db import models
from auditlog.registry import auditlog

class CourseSubject(BaseModel):
    code = models.CharField(max_length=5, unique=True)
    description = models.CharField(max_length=255)
    academic_unit = models.ForeignKey('academic_structure.AcademicUnit', on_delete=models.CASCADE, related_name='course_subjects')

    def __str__(self):
        return self.code

auditlog.register(CourseSubject)

class CourseTag(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

auditlog.register(CourseTag)

class Course(BaseModel):
    title = models.CharField(max_length=255)
    abbreviated_title = models.CharField(max_length=50, null=True, blank=True)
    number = models.CharField(max_length=8)
    subject = models.ForeignKey(CourseSubject, on_delete=models.CASCADE)
    credit_hours = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    tags = models.ManyToManyField(CourseTag, related_name='courses')
    special_topics_course = models.BooleanField(default=False)
    autogenerate_course_section_numbers = models.BooleanField(default=True)

    unlimited_capacity = models.BooleanField(default=False)
    allowed_grading_bases = models.ManyToManyField('grading.GradingBasis', related_name='courses')

    first_available_date = models.DateField(null=True, blank=True) # The first date that you can offer this course. Course sections can only start on or after this date.
    last_available_date = models.DateField(null=True, blank=True) # Controls when to retire the course.
    academic_level = models.ForeignKey('academic_structure.AcademicLevel', on_delete=models.SET_NULL, null=True, related_name='courses')
    hidden = models.BooleanField(default=False)

    course_inventory_owner = models.ForeignKey(AcademicUnit, on_delete=models.SET_NULL, null=True, related_name='course_inventories')
    offered_by = models.ManyToManyField(AcademicUnit, related_name='offered_courses')

    allowed_locations = models.ManyToManyField(Location, related_name='courses')

    public_notes = models.TextField(blank=True, null=True, help_text='Notes that students can view.')
    private_notes = models.TextField(blank=True, null=True, help_text='Notes that students can\'t view.')

    course_credits = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject.code}{self.number} - {self.title}"

auditlog.register(Course)