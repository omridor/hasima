from django.shortcuts import render
from parties.models import Party


def home(request):
    party_list = Party.objects.all()
    return render(request, 'home.html',dictionary={'party_list' : party_list})

