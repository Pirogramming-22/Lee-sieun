from django import forms
from .models import Ideas
from devTool.models import DevTool

class UserForm(forms.ModelForm):
    class Meta:
        model = Ideas
        exclude = ('is_starred', 'likes')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tool'].choices = [(tool.name, tool.name) for tool in DevTool.objects.all()]
    