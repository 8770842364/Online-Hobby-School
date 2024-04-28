from django.db import models

class mstuser(models.Model):
    sno=models.AutoField(primary_key=True)
    fnm=models.CharField(max_length=25)
    dob=models.DateField()
    gender=models.CharField(max_length=15)
    address=models.CharField(max_length=60)
    city=models.CharField(max_length=20)
    emailid=models.CharField(max_length=40)
    pwd=models.CharField(max_length=15)
    role=models.CharField(max_length=10)