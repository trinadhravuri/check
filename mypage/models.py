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
        