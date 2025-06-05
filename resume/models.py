from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_role = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class About(models.Model):
    profile_pic = models.ImageField(upload_to='photos/')
    experience = models.CharField(max_length=50)
    experience_role = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.experience_role
    
class Frontend_Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_logo = models.ImageField(upload_to='photos/')
    skill_level = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

class Backend_Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_logo = models.ImageField(upload_to='photos/')
    skill_level = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name
    
class Project(models.Model):
    project_image = models.ImageField(upload_to='photos/')
    project_name = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name
