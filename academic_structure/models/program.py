from core.models import BaseModel
from django.core.exceptions import ValidationError
from django.db import models
from auditlog.registry import auditlog

class ProgramOfStudyType(BaseModel):
    """
    Program of study type (ex: major, program, minor, concentration, etc.)
    """
    name = models.CharField(max_length=255)
    credential_granting = models.BooleanField(default=False)
    concentration_possible = models.BooleanField(default=False)
    can_stand_alone = models.BooleanField(default=False)

    levels_offered_at = models.ManyToManyField('academic_structure.AcademicLevel', related_name='program_of_study_types')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Program of Study Type'
        verbose_name_plural = 'Program of Study Types'

auditlog.register(ProgramOfStudyType)


class ProgramOfStudy(BaseModel):
    """
    Program of study (ex: Accounting **Major**, Art **Minor**, Clinical Psychology **Program**, Violin **Concentration**, etc.) 
    |> Note: bolded items represent the program of study type
    """
    effective_date = models.DateField()
    program_of_study_type = models.ForeignKey(ProgramOfStudyType, on_delete=models.SET_NULL, null=True, related_name='program_of_studies')

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16, blank=True, null=True)
    owning_academic_unit = models.ForeignKey('academic_structure.AcademicUnit', on_delete=models.SET_NULL, null=True, related_name='programs_of_study')
    academic_level = models.ForeignKey('academic_structure.AcademicLevel', on_delete=models.SET_NULL, null=True, related_name='programs_of_study')
    coordinating_academic_unit = models.ForeignKey('academic_structure.AcademicUnit', on_delete=models.SET_NULL, null=True, related_name='coordinating_programs_of_study')
    first_entry_date = models.DateField(null=True, blank=True)
    educational_credentials = models.ManyToManyField('academic_structure.EducationalCredential', related_name='programs_of_study')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Program of Study'
        verbose_name_plural = 'Program of Studies'

auditlog.register(ProgramOfStudy)

class EducationalCredentialType(BaseModel):
    """
    Credential type (ex: degree, certificate, etc.)
    """
    abbreviation = models.CharField(max_length=80)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Educational Credential Type'
        verbose_name_plural = 'Educational Credential Types'
auditlog.register(EducationalCredentialType)

class EducationalCredential(BaseModel):
    """
    Credential (ex: Bachelor of Science Degree, Bachelor of Arts Degree, Master of Science Degree, etc.)
    """
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    credential_type = models.ForeignKey(EducationalCredentialType, on_delete=models.SET_NULL, null=True, related_name='educational_credentials')
    # Include Type in Description Select this check box to display the credential type after the credential name in tasks and reports. Example: Bachelor of Science Degree.
    include_type_in_description = models.BooleanField(default=False)

    # Educational Credential Usage Specify when the credential is:
        # • External: Credentials from external educational institutions.
        # • Internal: Credentials that your institution confers.
    educational_credential_usage = models.CharField(max_length=255, blank=True, null=True, choices=[('External', 'External'), ('Internal', 'Internal')])

    def __str__(self):
        if self.include_type_in_description:
            return f"{self.name} {self.credential_type.name}"
        return self.name
    
    class Meta:
        verbose_name = 'Educational Credential'
        verbose_name_plural = 'Educational Credentials'

auditlog.register(EducationalCredential)