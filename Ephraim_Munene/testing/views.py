from django.shortcuts import render, redirect
from .models import Car


# Create your views here.
def index(request):
    data = Car.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        plate = request.POST.get('plate')

        if len(request.FILE) !=0:
            image = request.FILE['image']

    query=Car(name=name, year=year, plate=plate, image=image)
    query.save()
    return redirect('/')
    return render(request, "index.html")
