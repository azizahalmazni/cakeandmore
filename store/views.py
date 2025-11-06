from django.shortcuts import render

def store_home(request):
    return render(request, 'store/store.html')

def custom_cake(request):
    return render(request, 'store/custom_cake.html')
