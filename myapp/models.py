from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=25,blank=False, null=False)
    age=models.IntegerField()
    number=models.IntegerField()
    address=models.CharField(max_length=25,blank=False, null=False)

    def __str__(self):
        return self.name