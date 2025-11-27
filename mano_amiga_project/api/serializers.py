# Serializers for transforming data
"""
Create serializers to convert model instances to JSON format and vice versa.
"""
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Include all fields
