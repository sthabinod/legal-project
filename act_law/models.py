from django.db import models
from django.urls import reverse

class ActLaw(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20, unique=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], default='active')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actlaw_delete', args=[str(self.pk)])