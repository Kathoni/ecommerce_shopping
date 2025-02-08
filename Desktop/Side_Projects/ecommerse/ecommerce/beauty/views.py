from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

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
def mpesaapi(request):

 c1= MpesaClient()
 phone_number = '0111725146'
 amount = 1
 account_reference = 'reference'
 transaction_desc = 'Payment made with Mpesa'
 callback_url = 'https://darajambili.herokuapp.com/express-payment';
 response = c1.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
 return JsonResponse(response)

def stk_push_callback(request):
    data = request.body

    return HttpResponse('STK push call successful')