from django.shortcuts import render

# Create your views here.
def blog_home_view(request):
    return render (request,'blog/blog-home.html')

def blog_single_view(request):
    return render(request, 'blog/blog-single.html')