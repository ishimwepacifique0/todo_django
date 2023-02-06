from django.db import models

# Create your models here.

class StudentData(models.Model):
    StudentName = models.CharField(max_length=255)
    Option = models.CharField(max_length=255)
    Date = models.DateField()
    Level = models.CharField(max_length=255)
    Academic_year = models.CharField(max_length=255,default='2023')
    Expired = models.DateField()
    Request = models.CharField(max_length=255,default="Exam card")
    Gender = models.CharField(max_length=255,default="male")

    def __str__(self):
        return self.StudentName