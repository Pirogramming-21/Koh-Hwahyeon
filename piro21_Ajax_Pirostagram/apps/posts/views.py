from django.shortcuts import render, redirect
from .models import Post, User, Comment
from .forms import PostForm, CommentForm, SortForm

# Create your views here.
    
def main(request):
    sort_form = SortForm(request.GET)
    sort_by = request.GET.get('sort_by', '등록순')
    
    if sort_by == '이름순':
        posts = Post.objects.order_by('title')
    elif sort_by == '최신순':
        posts = Post.objects.order_by('-id')
    else:
        posts = Post.objects.order_by('id')

    context= {
        'posts':posts,
        'sort_form':sort_form,
    }
    return render(request, 'post_list.html', context)

def detail(request, pk):
    author=User.objects.get(id=pk)
    posts=Post.objects.filter(author=author)
    context={
        'author':author,
        'posts':posts,
    }
    return render(request, 'post_detail.html', context)

def create(request):
    if request.method=="GET":
        form=PostForm()
        context={'form':form}
        return render(request, 'post_create.html', context)
    
    form=PostForm(request.POST, request.FILES)
    if form.is_valid():
        post=form.save()
        return redirect('posts:main')
    context={'form':form}
    return render(request, 'post_create.html', context)

def delete(request, pk):
    post=Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(request, pk):
    post=Post.objects.get(id=pk)
    if request.method=="GET":
        form=PostForm(instance=post)
        context={'form':form, 'pk':pk}
        return render(request, 'post_update.html', context)
    
    form=PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect("posts:detail", pk=post.author.pk)
    
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def like_ajax(request):
    req=json.loads(request.body)
    post_id=req['id']
    button_type=req['type']

    post=Post.objects.get(id=post_id)

    if button_type=='like':
        post.like+=1

    elif button_type == 'cancel':
        post.like -= 1

    post.save()

    return JsonResponse({'id':post_id, 'like_count':post.like})

def search(request):
    search_txt = request.GET.get("search_txt", "")
    posts = Post.objects.all()
    if search_txt:
        posts = Post.objects.filter(title__icontains=search_txt)
        
    results = [
        {
            'title': post.title,
            'content': post.text,
            'author': post.author.name if post.author else 'Unknown',
            'created_at': post.created_date.strftime('%Y-%m-%d %H:%M:%S'),
            'image': post.image.url if post.image else '',
        } for post in posts
    ]

    return JsonResponse(results, safe=False)

@csrf_exempt   
def comment_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        post_id = data.get('post_id')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, content=content)
        comment.save()
        ret = {
            'content': comment.content,
            'comment_id': comment.id,
            'post_id':post_id
        }
        return JsonResponse(ret)
    
@csrf_exempt
def delete_comment_ajax(request):
    if request.method=="POST":
        data = json.loads(request.body)
        comment_id=data.get('comment_id')
        comment=Comment.objects.get(id=comment_id).delete()
        return JsonResponse({'success': True})
    
