from django.http import HttpResponse
from django.shortcuts import render
from planista.models import Company


def index(request):
    popular_companies = Company.objects.filter(views__gt = 10)
    return render(request, 'index.html', {'popular_companies': popular_companies})