from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Customer
from .forms import NewCustomerForm

def index(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "customers/index.html", {
            "title": "Easy Invoice - Kunden",
            "customers": Customer.objects.all()
        })


def edit(request, customer_id):
    customer = get_object_or_404(Customer, customer_id = customer_id)

    if request.method == 'POST':
        form = NewCustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/customers/")
    else:
        form = NewCustomerForm(instance=customer)

    return render(request, 'customers/edit.html', {
        "form": form, 
        "customer": customer,
        "title": "Easy Invoice - Kunde bearbeiten",
    })


def delete(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    customer.delete()
    return HttpResponseRedirect("/customers/")
    
    
def add_new(request):
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/customers/")
    else:
        form = NewCustomerForm()
        return render(request, "customers/add_new.html", {
            "title": "Easy Invoice - Neuer Kunden",
            "form": form
        })