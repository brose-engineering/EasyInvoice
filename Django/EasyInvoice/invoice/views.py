from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from invoice.models import Invoice

# Create your views here.
def index(request):
    if request.method == "POST":
        pass
    else:
        return render(request,'invoice/index.html',{
            "title": "Easy Invoice - Rechnungen",
            "invoices": Invoice.objects.all()
        })
    
def new(request):
    pass