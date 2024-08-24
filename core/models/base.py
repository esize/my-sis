from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.active = False
        self.save()

    class Meta:
        abstract = True
