from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserCreationForm

def loginpage(request):
    page = 'a'
    if request.user.is_authenticated:
        return redirect('my-account', pk=request.user.id)
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        if username:
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'User does not exist !')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('my-account', pk=user.id)
        else:
            messages.error(request, 'Incorrect username or password!')
    context = {'page' : page}
    return render(request, 'base/login_register.html', context)

def register_user(request):
    if request.user.is_authenticated:
        return redirect('my-account', pk=request.user.id)
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('my-account', pk=user.id)
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'base/login_register.html', {'form': form})

@login_required(login_url='/')
def my_account(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.user == user:
        if request.method == 'POST':
            if request.POST.get("user_age"):
                age = request.POST.get("user_age")
                user.age = age
            if request.POST.get("user_weight"): 
                weight = request.POST.get("user_weight")
                user.weight = weight  
            if request.POST.get("user_height"):
                height = request.POST.get("user_height")
                user.height = height
            if user.age and user.weight and user.height:
                user.completed_quiz = True
            user.save()
            return redirect('my-account', pk=user.id)
    return render(request, 'base/my_account.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('login')
