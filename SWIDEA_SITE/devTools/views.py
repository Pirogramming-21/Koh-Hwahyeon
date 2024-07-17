from django.shortcuts import render, redirect
from .models import DevTool
from ideas.models import Idea
from .forms import DevToolForm

# Create your views here.

def list(request):
    devtools=DevTool.objects.all()
    context={'devtools':devtools}
    return render(request, 'devTools/list.html', context)

def create(request):
    if request.method=="GET":
        form=DevToolForm()
        context={'form':form}
        return render(request, 'devTools/create.html', context)
    
    form=DevToolForm(request.POST)
    if form.is_valid():
        devtools=form.save()
    return redirect('devTools:detail', pk=devtools.pk)

def detail(request, pk):
    devtools=DevTool.objects.get(id=pk)
    related_ideas = Idea.objects.filter(tool=devtools)
    context = {'devtools': devtools, 'related_ideas': related_ideas}
    return render(request, 'devTools/detail.html', context)

def delete(request, pk):
    DevTool.objects.get(id=pk).delete()
    return redirect('devTools:list')

def update(request, pk):
    devtools=DevTool.objects.get(id=pk)
    if request.method=='GET':
        form=DevToolForm(instance=devtools)
        context={'form':form, 'pk':pk}
        return render(request, 'devTools/update.html', context)
    
    form=DevToolForm(request.POST, instance=devtools)
    if form.is_valid():
        form.save()
    return redirect('devTools:detail', pk)