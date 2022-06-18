from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')
