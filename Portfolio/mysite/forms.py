from django import forms
from .models import Costomer 
from django import forms




    

class Forms(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name','class':'input-field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':"Enter Your email",'class':'input-field'}))
    context = forms.CharField(widget=forms.Textarea(attrs={'placeholder':"Enter Your Message",'class':"input-field"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = '>Name'
        self.fields['email'].label = 'Email'
        self.fields['context'].label = 'Message'
    
    class Meta:
        model = Costomer
        fields = ('first_name','email','comments')