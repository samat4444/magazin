from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from .models import Category,Product
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render  
from django.shortcuts import redirect 

from .forms import SignUpForm


def product_list(request):
    template = loader.get_template('Product_list.html')
    blogs = Product.objects.all()
    category = Category.objects.all()
    context = {
        'blogs': blogs,
        'category':category
    }
    return HttpResponse(template.render(context, request))

    



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
            return redirect('product_list')
        else:
            form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})





def product_detail(request, pk, slug):
    blog = Product.objects.get(id=pk, slug=slug)
    context = {
        'blog':blog
        }
    return render(request, 'baza.html',context)

def category_filter(request, pk):
    blogs = Product.objects.filter(category=pk)
    categories = Category.objects.all()
    context = {
        'blogs':blogs,
        'categories':categories
        }
    return render(request, 'category.html',context)

    



