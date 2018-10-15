from django.shortcuts import render
from .models import User

def users_list(request):
    qs = User.objects.all().order_by('first_name')
    return render(request, 'users/users_list.html', {'users_list': qs})
