"""
Implement the views that perform the CRUD operations (e.g., creating, retrieving, updating, deleting students).
"""
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
