
from django import forms
from .models import Post

class WritePost(forms.ModelForm):  

    Title = forms.CharField(label="", required=True, max_length=30, widget=forms.TextInput(attrs={"placeholder": "Inserire il titolo"}))
    Description = forms.CharField(label="", required=True, max_length=500, widget=forms.Textarea())
    FPS_ex = forms.FloatField(label="", required=True, widget=forms.NumberInput(attrs={"placeholder": "Inserire gli FPS generati"}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta: 
        model = Post
        exclude =  ["P_ID_num", "user_id"]
        labels={
            'videogames_id': '',
            'computer_id': ''
        }


