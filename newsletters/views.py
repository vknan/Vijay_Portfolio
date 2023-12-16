from django.shortcuts import render, redirect
from .models import Subscriber
# Create your views here.
class newsletters:
    @staticmethod
    def subscribe(request):
        if request.method == 'POST':
            email = request.POST.get('email')
            if email is not None:
                existing_subscriber = Subscriber.objects.filter(email=email).first()
                if existing_subscriber:
                    error_message = 'Email is already subscribed'
                    return render(request, 'pages/index.html', {'error_message': error_message})
                else:
                    Subscriber.objects.create(email=email)
                    # Add code to send a confirmation email if desired
                    return redirect('success_page')
            else:
                error_message = 'Enter Email Address to Subscribe'
                return render(request, 'pages/index.html', {'error_message': error_message})
        return render(request, 'pages/index.html', {'email': email})
    @staticmethod
    def success_page(request):
        message = "successfully subscribed"
        return render(request, 'newsletters/success_page.html', {'message': message})
