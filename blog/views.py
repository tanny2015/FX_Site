from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse(123)  # 这个括号里边是什么，网页上就显示什么