from django.contrib import admin

from .models import AcademicUnit, AcademicUnitType, AcademicLevel, ProgramOfStudyType, ProgramOfStudy, EducationalCredential, EducationalCredentialType

admin.site.register(AcademicUnit)
admin.site.register(AcademicUnitType)
admin.site.register(AcademicLevel)
admin.site.register(ProgramOfStudyType)
admin.site.register(ProgramOfStudy)
admin.site.register(EducationalCredential)
admin.site.register(EducationalCredentialType)