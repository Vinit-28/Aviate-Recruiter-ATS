# Importing Dependencies #
from django.db import models


# Gender Choices #
class Gender(models.TextChoices):
    Male = 'Male', 'Male'
    Female = 'Female', 'Female'
    Other = 'Other', 'Other'


# Candidate Model #
class Candidate(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    age = models.IntegerField(null=False)
    gender = models.CharField(choices=Gender.choices, max_length=10)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(null=False, unique=True, max_length=20)

    def __str__(self):
        return f"Candidate {self.name} ({self.email}, {self.phoneNumber})."