"""
Define the Student model here, including fields like name, email, and any other relevant attributes.
"""
from django.db import models

class Student(models.Model):
    # Define the fields for the Student model
    id = models.AutoField(primary_key=True)  # Automatically incrementing ID
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.lastname}"
