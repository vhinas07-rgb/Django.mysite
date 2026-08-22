from django.db import models

# Create your models here.

# image =
# author = 
title = models.CharField(max_length=255)
content = models.TextField()
# tags = 
# category = 
counted_views = models.IntegerField(default=0)
status = models.BooleanField(default=False)
published_date = models.DateTimeField(null=True)
created_date = models.DateTimeField(auto_now_add=True)
updated_date = models.DateTimeField(auto_now=True)
#  / مدل فعلی Contact  
class Contact(models.Model):
    name = models.CharField(max_length=255)
email = models.EmailField()
subject = models.CharField(max_length=255)
message = models.TextField()
created_date = models.DateTimeField(auto_now_add=True)
updated_date = models.DateTimeField(auto_now=True)
