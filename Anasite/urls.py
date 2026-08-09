
from django.urls import path
from Anasite.views import *
urlpatterns = [
    path('',index_view),
    #path('blog',blog_view),
    path('about',about_view),
    path('contact',contact_view)
]
