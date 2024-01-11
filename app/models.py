from django.db import models

class Owners(models.Model):
    owner_id = models.CharField(max_length=100, primary_key=True)
    owner_name = models.CharField(max_length=250)
    owner_pass = models.CharField(max_length=250)
    owner_address = models.CharField(max_length=250,null=True)
    owner_tel = models.CharField(max_length=250,null=True)
    owner_email = models.CharField(max_length=250,null=True)
    timestamp = models.DateTimeField(null=True)
    
    
    
