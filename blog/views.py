from django.shortcuts import render
from django.http import JsonResponse
from.models import blog , blog_comment
import json
# Create your views here.
def blogs(request):
    blogs = blog.objects.all()
    
    return render(request , 'blog/blog.html' , {"blogs" : blogs})

def blog_detail(request , slug) :
    single_blog = blog.objects.get(slug=slug)
    comments = blog_comment.objects.filter(blog=single_blog , admin_vrify=True)
    return render(request , 'blog/single-blog.html', {'blog' : single_blog , 'comments' : comments})

def blog_comment_like(request) :
    data = json.loads(request.body.decode('utf-8'))
    comment_id = data.get('comment_id')
    comment = blog_comment.objects.filter(id=comment_id).first()
    if comment.has_user_disliked(request.user):
        return JsonResponse({"data" : '0' })
    if comment.has_user_liked(request.user):
        like = comment.like
        new_like = like - 1
        blog_comment.objects.filter(id=comment_id).update(like=new_like)
        comment.user_liked.remove(request.user)
        return JsonResponse({"data" : '2' })
    else :
        like = comment.like
        new_like = like + 1
        blog_comment.objects.filter(id=comment_id).update(like=new_like)
        comment.user_liked.add(request.user)
        return JsonResponse({"data" : '1' })

def blog_comment_dislike(request) :
    data = json.loads(request.body.decode('utf-8'))
    comment_id = data.get('comment_id')
    comment = blog_comment.objects.filter(id=comment_id).first()
    if comment.has_user_liked(request.user):
        print(0)
        return JsonResponse({"data" : '0' })
    if comment.has_user_disliked(request.user):
        like = comment.dislike
        new_like = like - 1
        blog_comment.objects.filter(id=int(comment_id)).update(dislike=new_like)
        comment.user_dislike.remove(request.user)
        print(2)
        return JsonResponse({"data" : '2' })
    else:
        like = comment.dislike
        new_dislike = like + 1
        blog_comment.objects.filter(id=int(comment_id)).update(dislike=new_dislike)
        comment.user_dislike.add(request.user)
        print(1)
        return JsonResponse({"data" : '1' })
    

def blog_comment_create(request):
    data = json.loads(request.body.decode('utf-8'))
    blog_id = data.get("blog_id")
    comment_text = data.get('tetx_value')
    Blog = blog.objects.filter(id=blog_id).first()
    new_comment = blog_comment(user=request.user , blog=Blog , text=comment_text)
    new_comment.save()
    return JsonResponse({'data':'1'})

def blog_reply(request):
    data = json.loads(request.body.decode('utf-8'))
    print('+'*34)
    print(data)
    print('+'*34)
    comment_id = data.get("comment_id")
    blog_id = data.get("blog_id")
    comment_text = data.get('comment_text')
    parent = blog_comment.objects.filter(id=comment_id).first()
    Blog = blog.objects.filter(id=blog_id).first()
    reply_to_comment = blog_comment(user=request.user, text=comment_text, parent=parent, blog=Blog)
    reply_to_comment.save()
    return JsonResponse({'data':'1'})