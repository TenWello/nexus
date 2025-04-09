from django.shortcuts import render


from .models import Blog

def blog_views(request):
    blogs = Blog.objects.all().order_by('-created_date')  # eng yangi bloglar birinchi chiqadi
    return render(request, 'blog.html', {'blogs': blogs})
