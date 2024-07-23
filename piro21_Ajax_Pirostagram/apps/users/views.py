from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.http import JsonResponse
from apps.posts.models import Post

def list(request):
    users=User.objects.all()
    context={'users':users}
    return render(request, 'user_list.html', context)

def create(request):
    if request.method=="GET":
        form=UserForm
        context={'form':form}
        return render(request, 'user_create.html',context)
    
    form=UserForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('users:list')

def delete(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('users:list')

def update(request, pk):
    user=User.objects.get(id=pk)
    if request.method=="GET":
        form=UserForm(instance=user)
        context={'form':form, 'pk':pk}
        return render(request, 'user_update.html', context)
    
    form=UserForm(request.POST, instance=user)
    if form.is_valid():
        form.save()

    return redirect('users:list')


def search_user(request):
    search_txt = request.GET.get('search_txt')
    users = User.objects.filter(name__icontains=search_txt)
    results = [{'id': user.id, 'name': user.name} for user in users]
    return JsonResponse(results, safe=False)


