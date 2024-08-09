from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Invoice
from .forms import newInvoiceForm


# Create your views here.
def index(request):
    if request.method == "POST":
        pass
    else:
        return render(request,'invoice/index.html',{
            "title": "Easy Invoice - Rechnungen",
            "invoices": Invoice.objects.all()
            # "invoices": Invoice.objects.all()
        })
    
def new(request):
    if request.method == "POST":
        form = newInvoiceForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/invoice/')
    else:
        form = newInvoiceForm()
        return render(request,'invoice/new.html',{
            "title": "Easy Invoice - Neue Rechnung",
            "form": form,
        })