from django.contrib.auth.models import User
from django.db import models
from auditlog.registry import auditlog
from .person import Person
from .base import BaseModel

class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.person.first_name} {self.person.last_name}"
auditlog.register(UserProfile)