from django.shortcuts import render
from django.views.generic import ListView
from .models import Testimonial, Project, Social, Info

# Create your views here.
def home(request):
    infos = Info.objects.all()
    projects = Project.objects.all()
    socials = Social.objects.all()
    testimonials = Testimonial.objects.all()
    context = {'infos': infos, 'projects': projects, 'socials': socials, 'testimonials': testimonials}
    return render(request, 'portfolio/index.html', context)

