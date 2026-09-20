from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):                      #فرخوانی دستی
    date_hierarchy = 'created_date'
    # fields = ('name' , 'title' , 'view_birth_date')
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','published_date')
    list_filter= ('status','author')
    ordering = ['created_date',]
    search_fields=['title','content']
admin.site.register(Post,PostAdmin)
