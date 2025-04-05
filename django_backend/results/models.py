from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    attendance = models.JSONField(default=dict)  # e.g., {"Mathematics": 90, "Physics": 85}
    ia1 = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    ia2 = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(20)]
    )
    ese = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(80)]
    )
    lab_attendance = models.FloatField(
        null=True, 
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    assignments = models.JSONField(default=list)  # e.g., [{"subjectName": "Mathematics", "marks": [15, 18, 20]}]
    practicals = models.JSONField(default=list)  # e.g., [{"labName": "Physics Lab", "grades": ["A", "B", "A"]}]
    email = models.EmailField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

    class Meta:
        ordering = ['roll_no']
        indexes = [
            models.Index(fields=['roll_no']),
            models.Index(fields=['email']),
        ]

    def save(self, *args, **kwargs):
        # Ensure JSON fields are properly initialized
        if not self.attendance:
            self.attendance = {}
        if not self.assignments:
            self.assignments = []
        if not self.practicals:
            self.practicals = []
        super().save(*args, **kwargs)

    def calculate_total(self):
        if self.ia1 is not None and self.ia2 is not None and self.ese is not None:
            ia_avg = (self.ia1 + self.ia2) / 2
            return round(ia_avg + self.ese, 2)
        return None
