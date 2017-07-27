from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
import datetime

# Create your views here.
def home(request):
    # return render(request, 'home.html', {}) # {}里边是参数
    # render_to_response 里淘汰了context_instance，详细看这里：https://stackoverflow.com/questions/38739422/django-error-render-to-response-got-an-unexpected-keyword-argument-context-i
    context = {'time':datetime.datetime.now()}
    return render(template_name='index.html',  context=context,request=request)




def contact(request):
    return render(template_name='contact.html',request=request)