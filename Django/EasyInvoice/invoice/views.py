from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from customers.models import Customer

# Create your views here.
def index(request):
    return HttpResponse(f"Hello there!")