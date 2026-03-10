from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# Pages
def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'store/profile.html'  # Change this to your profile template


#Registe/Login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Registration failed. Please check the form.")
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/registration/register.html', {'form': form})

#UpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'store/profile.html', {'form': form})

