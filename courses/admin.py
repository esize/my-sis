from django.contrib import admin
from .models import Course, CourseSubject, CourseTag, CourseSection, CourseSectionType, CourseMeetingPattern, CourseMeetingDays, CourseMeetingPeriod

admin.site.register(Course)
admin.site.register(CourseSubject)
admin.site.register(CourseTag)
admin.site.register(CourseSection)
admin.site.register(CourseSectionType)
admin.site.register(CourseMeetingPattern)
admin.site.register(CourseMeetingDays)
admin.site.register(CourseMeetingPeriod)