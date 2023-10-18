from django.db import models
from django.contrib import admin
class Football_player(models.Model):
    Name=models.CharField(max_length=15)
    Age=models.IntegerField()
    DOB=models.CharField(max_length=10)
    Jerseynumber=models.IntegerField()
    Email=models.EmailField()
class Football_playerAdmin(admin.ModelAdmin):
    list_display=('Name','Age','DOB','Jerseynumber','Email')

# create your models here.
