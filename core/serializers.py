from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'created_at', 'updated_at', 'legal_name', 'preferred_name','personal_email', 'date_of_birth', 'phone_numbers', 'addresses']
        depth=2

        