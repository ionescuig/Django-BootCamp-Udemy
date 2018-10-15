from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    dict = {'insert_me': 'Please go to /users to see the users.'}
    return render(request,'AppTwo/index.html', context=dict)

def help(request):
    dict = {'insert_me': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=dict)
