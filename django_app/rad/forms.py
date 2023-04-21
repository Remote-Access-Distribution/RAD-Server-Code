from django import forms
from django.forms import widgets
from django.utils import timezone

from .models import Traders
from .models import Distros
from .models import TraderToDistro

# Creates forms based on the corresponding model defined in models.py

class TradersForm(forms.ModelForm):
    class Meta:
        model = Traders
        fields = ['trader_name']
        labels = {
            'trader_name': 'Trader Name',
        }
    
class DistrosForm(forms.ModelForm):
    class Meta:
        model = Distros
        fields = ['distro_location', 'socket_count']
        labels = {
            'distro_location': 'Distro Location',
            'socket_count': 'Socket Count',
        }

class TraderToDistrosForm(forms.ModelForm):
    class Meta:
        model = TraderToDistro
        fields = ['trader','distro','socket_number','start_time']
        labels = {
            'socket_number': "Socket Number",
            'start_time': "Start Date",
        }
        widgets = {
           'start_time': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
       }
