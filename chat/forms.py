# from django import forms
# from .models import history

# class historyForm(forms.ModelForm):
#     class Meta:
#         model = history
#         fields = ['input','response']
#         widgets = {
#             'input': forms.TextInput(attrs={'placeholder': 'Enter you idea'}),
#             'response': forms.Textarea(attrs={'placeholder': 'Here is your response'}),
#         }


# chat/forms.py
# chat/forms.py

from django import forms

class UserInputForm(forms.Form):
    content = forms.CharField(
        label='Enter your input',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Type your video idea...'})
    )
