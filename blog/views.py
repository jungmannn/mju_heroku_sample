from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog=Blog()
    blog.title=request.POST['title']
    blog.body= request.POST['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk = blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blog/' + str(blog.id))
    else:
        return render(request,'edit.html',{'blog':blog})
def delete(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/')
    
 
