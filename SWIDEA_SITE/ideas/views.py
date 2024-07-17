from django.shortcuts import render, redirect
from .models import Idea, IdeaStar
from django.http import HttpResponse
from .forms import IdeaForm, SortForm
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def main(request):
    sort_form = SortForm(request.GET)
    sort_by = request.GET.get('sort_by', '등록순')
    
    if sort_by == '찜하기순':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif sort_by == '이름순':
        ideas = Idea.objects.order_by('title')
    elif sort_by == '최신순':
        ideas = Idea.objects.order_by('-id')
    else:
        ideas = Idea.objects.order_by('id')

    paginator = Paginator(ideas, 4) 
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj,
        'sort_form': sort_form,
    }
    return render(request, 'ideas/list.html', context)

def toggle_star(request, idea_id):
    if request.method == "POST":
        idea = Idea.objects.get(id=idea_id)

        star, created = IdeaStar.objects.get_or_create(idea=idea)
        if not created:
            star.delete()
            return HttpResponse("false")

        return HttpResponse("true")
    
def update_interest(request, idea_id, action):
    if request.method == "POST":
        idea = Idea.objects.get(id=idea_id)

        if action == 'increase':
            idea.interest += 1
        elif action == 'decrease':
            idea.interest -= 1
        idea.save()
        return HttpResponse(str(idea.interest))
    
def create(request):
    if request.method=="GET":
        form=IdeaForm()
        context={'form':form}
        return render(request, 'ideas/create.html', context)
    
    form=IdeaForm(request.POST, request.FILES)
    if form.is_valid():
        idea=form.save()
        return redirect('ideas:detail', pk=idea.pk)
    context = {'form': form}
    return render(request, 'ideas/create.html', context)

def detail(request, pk):
    idea=Idea.objects.get(id=pk)
    is_starred=IdeaStar.objects.filter(idea=idea).exists()
    context={'idea':idea, 'is_starred':is_starred}
    return render(request, 'ideas/detail.html', context)

def delete(request, pk):
    Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(request, pk):
    idea=Idea.objects.get(id=pk)
    if request.method=='GET':
        form=IdeaForm(instance=idea)
        context={'form':form, 'pk':pk}
        return render(request, 'ideas/update.html', context)
    
    form=IdeaForm(request.POST, request.FILES, instance=idea)
    if form.is_valid():
        form.save()
        return redirect('ideas:detail', pk=pk)
    context = {'form': form, 'pk': pk}
    return render(request, 'ideas/update.html', context)
    