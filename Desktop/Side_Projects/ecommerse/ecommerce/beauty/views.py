from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ensure this template exists
def about(request):
    return render(request, 'about.html')
