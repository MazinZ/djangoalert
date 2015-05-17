from django import forms
from alerts.models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['alertName','alertText','latitude','longitude']
