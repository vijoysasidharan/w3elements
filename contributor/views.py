from django.http.response import HttpResponse
from django.shortcuts import render
from django_hosts.resolvers import reverse

def homepage(request):
    homepage_url = reverse('homepage', host='www')
    return render(request, 'homepage.html', {'homepage_url': homepage_url})
    
def login(request):
    return render(request, "contributor/index.html")
