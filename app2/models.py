from django.db import models


#class Students(models.Model):
#    first_name=models.CharField(max_length=50)
#    last_name=models.CharField(max_length=50)
#    contact=models.IntegerField()
#    email=models.CharField(max_length=100)
#    age=models.IntegerField
#    media_imge=models.ImageField(upload_to="media/",max_length=250,null=True,default=None)
#def __str__(self):
#    pass
from django.db import models
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    econtact=models.CharField(max_length=15)
class Meta:
    db_table="employee"
