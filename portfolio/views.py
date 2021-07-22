from django.shortcuts import render
from django.views.generic import ListView
from .models import Testimonial, Project, Social, Info, Skill

# Create your views here.
def home(request):
    infos = Info.objects.all()
    projects = Project.objects.all()
    socials = Social.objects.all()
    testimonials = Testimonial.objects.all()
    skills = Skill.objects.all().order_by('-percentage')
    context = {'infos': infos, 'projects': projects, 'socials': socials, 'testimonials': testimonials, 'skills': skills}
    return render(request, 'portfolio/index.html', context)

