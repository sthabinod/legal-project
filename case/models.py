from django.db import models
from django.urls import reverse

class CaseSubType(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20, unique=True)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('निष्क्रिय', 'निष्क्रिय'),
        ('सक्रिय', 'सक्रिय'),
    ], default='सक्रिय')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('case_subtype_delete', args=[str(self.pk)])
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()
        
class CaseStage(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('निष्क्रिय', 'निष्क्रिय'),
        ('सक्रिय', 'सक्रिय'),
    ], default='सक्रिय')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('case_subtype_delete', args=[str(self.pk)])
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()
        

class CaseType(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('निष्क्रिय', 'निष्क्रिय'),
        ('सक्रिय', 'सक्रिय'),
    ], default='सक्रिय')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()
        
class CaseReportd(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('निष्क्रिय', 'निष्क्रिय'),
        ('सक्रिय', 'सक्रिय'),
    ], default='सक्रिय')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()