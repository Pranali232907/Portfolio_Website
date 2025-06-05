from django.contrib import admin
from .models import *

# Register your models here.
 
admin.site.register(User)
admin.site.register(About)
admin.site.register(Frontend_Skill)
admin.site.register(Backend_Skill)
admin.site.register(Project)