from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('elder', 'Elder'),
        ('helper', 'Helper'),
    )
     
    role = models.CharField(max_length=15, choices=ROLES)
    mobile = models.CharField(max_length=15, unique=True, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return f"{self.username} ({self.role})"

 
class Task(models.Model):
    TASKS = (
        ('medicine', 'Medicine Delivery'),
        ('care', 'Care Taker'),
        ('cook', 'Home Cook'),
        ('grocery', "Grocery"),
        ('walk', 'Walk'),
        ('other', 'Other'),
    )
    STATUS = (
        ('open', 'Open'),
        ('assigned', 'Assigned'),
        ('completed', 'Completed')
    )

    task = models.CharField(max_length=50, choices=TASKS)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='open')
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="accepted_task",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task} ({self.status})"
