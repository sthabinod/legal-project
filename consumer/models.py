from django.db import models
from nepali_datetime_field.models import NepaliDateField

GENDER_CHOICES = [
        ('male', 'पुरुष'),
        ('female', 'महिला'),
        ('others', 'अन्य'),
    ]

class Consumer(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    email_address = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15,unique=True)
    citizenship_no = models.CharField(max_length=20)
    citizenship_issue_district = models.CharField(max_length=200)
    citizenship_issue_date = models.DateField()
    grandfather_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.full_name

class PermanentAddress(models.Model):
    state= models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    ward = models.IntegerField()
    consumer = models.OneToOneField(Consumer,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.state}  {self.district} {self.municipality}"
    
class TemporaryAddress(models.Model):
    state= models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    ward = models.IntegerField()
    consumer = models.OneToOneField(Consumer,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.state}  {self.district} {self.municipality}"