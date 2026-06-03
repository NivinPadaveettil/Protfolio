from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactInquiry

def index(request):
    success = False
    
    if request.method == "POST":
        # Pull details using the 'name' attributes from your HTML inputs
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create record in the database if fields are filled
        if name and email and message:
            ContactInquiry.objects.create(
                name=name, 
                email=email, 
                subject=subject or 'No Subject',
                message=message
            )
            success = True
    
    return render(request, 'index.html', {'success': success})

def contact_view(request):
    success = False
    
    if request.method == "POST":
        # Pull details using the 'name' attributes from your HTML inputs
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create record in the database if fields are filled
        if name and email and message:
            ContactInquiry.objects.create(
                name=name, 
                email=email, 
                subject=subject or 'No Subject',
                message=message
            )
            success = True
            
    # Redirect to index with contact section
    return redirect('index')