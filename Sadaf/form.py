from .models import Subscriber
from django import forms

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name','email',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'subscribe-form-input w-100 text-truncate mx-auto my-2 container', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'subscribe-form-input w-100 text-truncate mx-auto my-2 container', 'placeholder': 'Email Address'}),
        }
        labels = {
            'name': '',
            'email': '',
        }
        
    def __init__(self, *args, **kwargs):
        super(SubscriberForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'subscribe-form-input w-100 text-truncate mx-auto my-2 container', 'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update({'class': 'subscribe-form-input w-100 text-truncate mx-auto my-2 container', 'placeholder': 'Email Address'})
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        