from django import forms
from .models import Post

class PostForm(forms.ModelForm):  #이 form이 ModelForm이라고 알려주기

    class Meta:    
        model = Post    #폼 만들기 위해서 어떤 model이 쓰여야 하는지 알려주기
        fields = ['title', 'text']