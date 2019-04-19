from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    output = ', '.join([str(mineral) for mineral in minerals])
    return HttpResponse(output)
