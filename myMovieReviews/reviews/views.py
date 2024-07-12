from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Review
from .forms import GenreForm

# Create your views here.
def reviews_list(request):
    reviews=Review.objects.all()
    return render(request, 'reviews_list.html', {'reviews':reviews})

def reviews_create(request):
    if request.method=="POST":
        form=GenreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/reviews/')
        else:
            return render(request, 'reviews_create.html', {'form': form})  
    else:
        form = GenreForm()
        return render(request, 'reviews_create.html', {'form': form})

def reviews_detail(request, pk):
    review=Review.objects.get(id=pk)
    converted_time=convert_time(review.time)
    context= {
        "review":review,
        "title":review.title,
        "year":review.year,
        "genre":review.genre,
        "star":review.star,
        "time":converted_time,
        "newreview":review.newreview,
        "director":review.director,
        "actor":review.actor,
    }
    return render(request, 'reviews_detail.html', context)

def reviews_update(request, pk):
    review=Review.objects.get(id=pk)
    if request.method=="POST":
        form=GenreForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            if 'image' not in request.FILES:
                form.cleaned_data['image'] = review.image

            form.save()
            
            return redirect(f"/reviews/{pk}/")
    else:
        form = GenreForm(instance=review)
    context = {
        'review': review,
        'form': form
    }
    return render(request, 'reviews_update.html', context)

def reviews_delete(request, pk):
    if request.method=="POST":
        review=Review.objects.get(id=pk)
        review.delete()
    return redirect('/reviews/')

def convert_time(minutes):
    if minutes:
        try:
            minutes=int(minutes)
            hours=minutes//60
            mins=minutes%60
            return f"{hours}시간 {mins}분"
        except:
            return "시간 정보 없음"