from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile", null=True, blank=True)
    Name = models.CharField(max_length=100)  
    Department = models.CharField(max_length=30, default="null")
    Roll_No = models.CharField(max_length=20, unique=True)  
    Birth_Date = models.DateField(default="2000-01-01")
    Email = models.EmailField(unique=True) 
    Contact_No = models.CharField(max_length=10, unique=True)  
    Admission_No = models.CharField(max_length=20, unique=True) 
    Academic_Year = models.CharField(max_length=9, default="2024-25")  
    address = models.TextField(blank=True, null=True)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)

    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)
    father_contact = models.CharField(max_length=15, blank=True, null=True)
    father_email = models.EmailField(blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)
    mother_contact = models.CharField(max_length=15, blank=True, null=True)

    health_issues = models.TextField(blank=True, null=True)

    SSC_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    SSC_year_of_passing = models.PositiveIntegerField(blank=True, null=True)
    SSC_board = models.CharField(max_length=100, blank=True, null=True)

    HSC_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    HSC_year_of_passing = models.PositiveIntegerField(blank=True, null=True)
    HSC_board = models.CharField(max_length=100, blank=True, null=True)

    sem1_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem2_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem3_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem4_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem5_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem6_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem7_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sem8_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.Name
