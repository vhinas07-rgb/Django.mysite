from django.db import models
from django.contrib.auth.models import User  

class Post(models.Model):          #بدون ارث بری از models.Model ،پست یه کلاس معمولیه که ارتباطی با دیتابیس نداره !
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User , on_delete = models.SET_NULL , null = True)
    title = models.CharField(max_length = 255)                       #attribute 
    content = models.TextField()
    # tags = 
    # category = 
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
        verbose_name= 'POST'
        verbose_name_plural= 'POSTS'
    def __str__(self):
        return self.title
