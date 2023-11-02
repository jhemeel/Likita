from django.db import models
from base.models import User
from datetime import datetime
import uuid

# Create your models here.
class Appointment(models.Model):
    
    class Service(models.TextChoices):
        CONSULTATION = "Consultation", "Consultation"
        HOME_CARE_SERVICES = "Home care service", "Home care services"
        LABORATORY_SERVICES ="laboratory services", "laboratory services"
        COUNSELLING = "Counselling", "Counselling"
        BASIC_ASSISTANCE = "Basic assistance care", "Basic assistance care"
        SECOND_OPINION = "Second opinion", "Second opinion"
    
    
    class Time(models.TextChoices):
        TIME_1 ="3 PM", "3:00 PM"
        TIME_2= "3:30 PM", "3:30 PM"
        TIME_3="4 PM", "4:00 PM"
        TIME_4="4:30 PM", "4:30 PM"
        TIME_5="5 PM", "5:00 PM"
        TIME_6="5:30 PM", "5:30 PM"
        TIME_7="6 PM", "6:00 PM"
        TIME_8="6:30 PM", "6:30 PM"
        TIME_9="7 PM", "7:00 PM"
        TIME_10="7:30 PM", "7:30 PM"
    
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='appointment_user')
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=Service.choices, default="Consultation")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=Time.choices, default="3 PM")
    phone = models.CharField(max_length=20)
    message = models.TextField(default="optional..")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name_plural = 'Appointment'
        ordering = ['-updated_at', '-created_at']
        
    def __str__(self):
        return f"{self.name.username} | day: {self.day} | time: {self.time}"


