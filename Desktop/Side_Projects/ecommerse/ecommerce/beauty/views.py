from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ensure this template exists
def about(request):
    return render(request, 'about.html')
def dry(request):
    return render(request,'dry.html')
def oily(request):
    return render(request,'oily.html')
def combination(request):
    return render(request,'combination.html')
