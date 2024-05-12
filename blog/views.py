from django.shortcuts import render
from.models import blog , blog_comment
# Create your views here.
def blogs(request):
    blogs = blog.objects.all()
    
    return render(request , 'blog/blog.html' , {"blogs" : blogs})

def blog_detail(request , slug) :
    single_blog = blog.objects.get(slug=slug)
    comments = blog_comment.objects.filter(blog=single_blog , admin_vrify=True)
    print('-'*88)
    print(single_blog)
    print(comments)
    print('-'*88)
    return render(request , 'blog/single-blog.html', {'blog' : single_blog , 'comments' : comments})
