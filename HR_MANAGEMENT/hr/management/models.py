from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#creating fields for table

class empdata(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=30)
    doj=models.CharField(max_length=20)
    expsalary=models.IntegerField()
    prevexp=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
