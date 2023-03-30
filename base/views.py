from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Query

# Create your views here.


def index(request):
    template_name = 'base/index.html'
    context = {}
    return render(request, template_name, context)


def formSumit(request):
    if request.method == 'POST':
        query = Query()
        query.name = request.POST.get('name')
        query.phone = request.POST.get('phone')
        query.email = request.POST.get('email')
        query.save()

        email = request.POST.get('email')
        send_mail(
            'Mail Has Been Sent!',
            'Your Mail has been sent, We will get back you soon.',
            'rahuly@parasightsolutions.com',
            [email],
            fail_silently=False
        )
        send_mail(
            'New query from the website',
            'You have recieved a new query from the website.',
            'rahuly@parasightsolutions.com',
            ['rahuly@parasightsolutions.com'],
            fail_silently=False
        )

        return redirect('success')
    else:
        template_name = 'base/index.html'
        return render(request, template_name)


def success(request):
    template_name = 'base/success.html'
    context = {}
    return render(request, template_name, context)
