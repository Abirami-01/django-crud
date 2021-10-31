from django import forms
from django.db.models import fields
from vehicle.models import veh

# Create your models here.
class vehForm(forms.ModelForm):
    class Meta:
        model = veh
        fields = '__all__'
   
