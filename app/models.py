from django.db import models

# Create your models here.
class Topics(models.Model):
    topic_name=models.CharField(max_length=40,primary_key=True)
    def __str__(self):
        return self.topic_name  

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topics,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    url=models.URLField(max_length=100,unique=True)
    def __str__(self):
        return self.name  
    
   

class Access_Record(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(max_length=40)
    
