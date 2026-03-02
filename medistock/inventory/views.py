from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicine
from .forms import MedicineForm
from datetime import date
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# --- Auth & Main Navigation Views ---

def index(request):
    """Landing page with Login, Help, Signup buttons."""
    return render(request, 'inventory/index.html')

def signup_view(request):
    """Handles user signup."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/signup.html', {'form': form})

def login_view(request):
    """Handles user login."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST) # Pass request to AuthenticationForm
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def logout_view(request):
    """Handles user logout."""
    logout(request)
    return render(request, 'inventory/logout_success.html')

@login_required(login_url='login')
def welcome(request):
    """Welcome page after login."""
    return render(request, 'inventory/welcome.html')

def help_view(request):
    """Help page."""
    return render(request, 'inventory/help.html')

# --- Inventory Views ---

@login_required(login_url='login')
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'inventory/medicine_list.html', {
        'medicines': medicines,
        'today': date.today()
    })

@login_required(login_url='login')
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')
    else:
        form = MedicineForm()

    return render(request, 'inventory/add_medicine.html', {'form': form})

@login_required(login_url='login')
def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    medicine.delete()
    return redirect('medicine_list')

@login_required(login_url='login')
def remove_expired(request):
    Medicine.objects.filter(expiry_date__lt=date.today()).delete()
    return redirect('medicine_list')
