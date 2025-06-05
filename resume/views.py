from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages                     
from .models import *
 
def contact(request):
    context = {
        "users": User.objects.all(),
        "abouts": About.objects.all(),
        "frontend_skills": Frontend_Skill.objects.all(),
        "backend_skills": Backend_Skill.objects.all(),
        "projects": Project.objects.all(),
    }
    return render(request, 'home.html', context)


