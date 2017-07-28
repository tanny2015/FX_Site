from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib.auth import authenticate,login as auth_login ,logout
from blog.forms import SignupForm
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    # return render(request, 'home.html', {}) # {}里边是参数
    # render_to_response 里淘汰了context_instance，详细看这里：https://stackoverflow.com/questions/38739422/django-error-render-to-response-got-an-unexpected-keyword-argument-context-i
    context = {'time':datetime.datetime.now()}
    return render(template_name='index.html',  context=context,request=request)


def about(request):
    return render(request, 'about.html', locals())


def signup(request):
    path = request.get_full_path()
    if request.method == 'POST':
        form = SignupForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            UserModel = get_user_model()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = UserModel.objects.create_user(username=username, email=email, password=password)
            user.save()
            auth_user = authenticate(username=username, password=password)
            auth_login(request, auth_user)
            return redirect("home")
    else:
        form = SignupForm(auto_id="%s")
    return render(request, 'signup.html', locals())


def logout_view(request):
    logout(request)
    return redirect('home')