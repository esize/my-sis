from rest_framework import serializers
from .models import *


class AcademicUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicUnit
        fields = '__all__'
        depth = 2


class AcademicUnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicUnitType
        fields = '__all__'
        depth = 2

class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'
        depth = 2

class ProgramOfStudyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramOfStudyType
        fields = '__all__'
        depth = 2

class ProgramOfStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramOfStudy
        fields = '__all__'
        depth = 2

class EducationalCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalCredential
        fields = '__all__'
        depth = 2

class EducationalCredentialTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalCredentialType
        fields = '__all__'
        depth = 2