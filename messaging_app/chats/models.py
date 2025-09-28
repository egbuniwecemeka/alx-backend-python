from django.db import models
import uuid


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password_hash = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    role = models.CharField(max_length=10, choices=[('guest', 'Guest'), ('host', 'Host'), ('admin', 'Admin')], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
