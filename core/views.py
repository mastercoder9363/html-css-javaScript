from django.shortcuts import render
from .models import *
def ind(request):
    tops = TopPost.objects.all()
    context = {
        "tops": tops
    }
    return render(request, 'index.html', context)
