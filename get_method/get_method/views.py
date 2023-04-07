from django.shortcuts import render, HttpResponse

def home(request):
    if request.method == 'GET':
        name = ['a','x','z']
    context = {
        'name': name
    }
    return render(request,'home.html',context)