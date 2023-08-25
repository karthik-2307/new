from django.shortcuts import render
def index(request):
    return render(request, "product/index.html")
def home_view(request):
    return render(request, 'product/images.html')
def about_view(request):
    return render(request, 'product/advanced.html')