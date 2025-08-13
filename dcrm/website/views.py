from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm ,add_records_forms
from .models import Record
def home(request):
    records = Record.objects.all();
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password= password)
        if user is not None:
            login(request , user)
            messages.success(request ,"You have been successfully logged in.")
            return redirect('home')
        else:
            messages.success(request , "There was an error logging . Please Try again")
            return redirect('home')
    else: 
        return render(request , 'home.html', {'records':  records})
        
        
def logout_user(request):
    logout(request)
    messages.success(request , "You have been successfully logged in.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed. Please try logging in.")
                return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def customer_records(request , pk):
    if request.user.is_authenticated:
        customer_records = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_records': customer_records})
    
    else:
        messages.success(request , "You must log in to access required feature...")
        return redirect('home')
    
def delete_records(request , pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request , "You have successfully deleted the record")
        return redirect('home')
    else:
        messages.success(request , "You must log in to access required feature...")
        return redirect('home')
    
    
def add_records(request):
    form = add_records_forms(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request , "You have successfully added a record")
                return redirect('home')
            
        return render(request, 'add_record.html', {'form': form})
    
    
def update_records(request, pk):
    if request.user.is_authenticated:
        customer_records = Record.objects.get(id=pk)
        form = add_records_forms(request.POST or None ,instance=customer_records)
        if form.is_valid():
            update_record = form.save()
            messages.success(request , "You have successfully updated a record")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request , "You must log in to access required feature...")
        return redirect('home')