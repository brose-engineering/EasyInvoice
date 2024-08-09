from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html', {
        "title": "Easy Invoice",
        "subtitle": "Das Rechnungsprogramm für Kleinunternehmer"
    })