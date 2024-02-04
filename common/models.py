from django.db import models
from django.urls import reverse

class Designation(models.Model):
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
        return reverse('designation_delete', args=[str(self.pk)])
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()
        

class JudgeCommittee(models.Model):
    name = models.CharField(max_length=255)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='judge_committee')
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
       
class DocumentType(models.Model):
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
        

class FiscalYear(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
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
        
         
class OfficeWard(models.Model):
    ward_no = models.CharField(max_length=255)
    ward_name= models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[
        ('निष्क्रिय', 'निष्क्रिय'),
        ('सक्रिय', 'सक्रिय'),
    ], default='सक्रिय')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.ward_name
    
    def delete(self, using=None, keep_parents=False):
        # Soft delete by updating is_deleted field
        self.is_deleted = True
        self.save()
        
