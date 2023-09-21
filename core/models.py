from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Patient(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Appointment(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[(
        'Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')])

    def __str__(self) -> str:
        return f"Appointment for {self.patient} on {self.appointment_date}"


class Doctor(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Hospital(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     zip_code = models.CharField(max_length=10, blank=True, null=True)

#     def __str__(self):
#         return self.name


class MedicalRecord(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_date = models.DateTimeField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    notes = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    # hospital = models.ForeignKey(
    #     Hospital, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"Medical record for {self.patient} on {self.record_date}"
