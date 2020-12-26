from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

Git_user_data = [
        {'user' : 'hdoyle1999',
        'repo' : 'HarryDoyle99',
        'date_created' : '21/6/2020'
        }
    ]

def home(request):
    Git_user_data[0]['user'] = 'doyleh4'
    

    data = {
        'Git_user_data' : Git_user_data
    }
    return render(request, 'visualiser/home.html', data)

def about(request):
    return render(request, 'visualiser/about.html', {'title':'About'})