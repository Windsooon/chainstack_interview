import uuid
from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
