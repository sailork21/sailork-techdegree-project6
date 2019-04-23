import random
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    #course = Course.objects.get(pk=pk)
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


def mineral_random(request, pk):
    #course = Course.objects.get(pk=pk)
    pk = random.randint(1, 875)
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})
