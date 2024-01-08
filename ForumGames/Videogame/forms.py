
from django import forms
from .models import PossVideogames


class addFormVideogame(forms.ModelForm):

    class Meta:
        model = PossVideogames
        fields=["name", "Description"]
        labels={
            'name': '',
            'Description': '',
        }
        widgets={
            'name':forms.TextInput(attrs={'placeholder':"Nome videogioco"}),
            'Description':forms.Textarea(attrs={"placeholder":"Descrizione"})
        }

    def saveVideogame(self, request):
        game = PossVideogames()
        game.name = self.cleaned_data['name']
        game.Description = self.cleaned_data['Description']
        game.user_id = request.user
        game.save()
