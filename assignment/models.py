from django.db import models
from django.contrib.auth.models import User

# Create your models here.
WORK_TYPES= (
    ("Youtube", "YOUTUBE"),
    ("Instagram", "INSTAGRAM"),
    ("Others", "OTHERS")
)
class client_table(models.Model):

    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    


class Work_table(models.Model):
    Link = models.CharField(max_length=100)
    work_type = models.CharField(choices=WORK_TYPES,max_length=30,default="None")
    def __str__(self):
        return self.work_type

class Artist_table(models.Model):
    name = models.CharField(max_length=30)
    work = models.ManyToManyField(Work_table,max_length=50)
    def __str__(self):
        return self.name




    

    