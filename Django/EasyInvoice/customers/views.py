from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm

form = CustomerForm

def index(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'customers/index.html', {
            "title": "Easy Invoice - Kunden",
            "customers": Customer.objects.all()
        })

def details(reqest):
    pass

def add_new(request):
    if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(request, 'customers/index.html')  # Replace 'index' with the name of your view or URL pattern
    else:
        form = CustomerForm()
        return render(request, 'customers/add_new.html', {'form': form})

def edit(request):
    pass