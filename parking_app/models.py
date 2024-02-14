from django.db import models
from datetime import datetime

# Create your models here.

class category(models.Model):
    PARKING_STATUS_CHOICES = [
        ('activated', 'Activated'),
        ('deactivated', 'Deactivated'),
    ]
    parking_area_number = models.CharField(max_length=10, blank=False, null=False)
    vehicle_type = models.CharField(max_length=30, blank=False, null=False)
    vehicle_limit = models.CharField(max_length=20, blank=False, null=False)
    parking_charge = models.CharField(max_length=10, blank=False, null=False)
    status = models.CharField(max_length=20, choices=PARKING_STATUS_CHOICES, default= 'activated')
    doc = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.parking_area_number

class vehicle_entry(models.Model):
    VEHICLE_STATUS_CHOICES = [
        ('parked', 'Parked'),
        ('leaved', 'Leaved'),
    ]
    vehicle_no = models.CharField(max_length=11, null=False, blank=False)
    parking_area_number = models.ForeignKey(category, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=30, blank=False, null=False)
    parking_charge = models.CharField(max_length=10, blank=False, null=False)
    status = models.CharField(max_length=20, choices=VEHICLE_STATUS_CHOICES, default='parked')
    arrival_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.vehicle_no