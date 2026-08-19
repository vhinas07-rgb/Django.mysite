from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

counted_views = models.IntegerField(default=0)
status = models.BooleanField()
published_date = models.DateTimeField()
created_date = models.DateField(auto_now_add=True)
updated_date = models.DateTimeField(auto_now=True)
# published_date = models.DateTimeFiled()