from django.db import models

# Create your models here.
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_img = models.ImageField(upload_to='media')
    skill_quote = models.CharField(max_length=350)
    skill_desc = models.TextField(max_length=10000)

    def __str__(self):
        return self.skill_name
    
    class Meta:
        verbose_name_plural = 'Skills'

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_img = models.ImageField(upload_to='media',null=True)
    Project_quote = models.CharField(max_length=500)
    project_teamsize = models.IntegerField()
    project_roles = models.TextField(max_length=10000)
    project_skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name_plural = 'Projects'

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact= models.BigIntegerField()
    message = models.CharField(max_length=1000)
    content = models.TextField(max_length=100000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Enquiries'

class downloadcv(models.Model):
    file = models.FileField(upload_to='media',null=True)