from .models import UserQuestion, OwnerAnswer
from django import forms


class UserQuestionForm(forms.ModelForm):
    class Meta:
        model = UserQuestion
        fields = ['content']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Your question'
        self.fields['content'].widget.attrs['class'] = 'question-form'
        self.fields['content'].label = ''
        