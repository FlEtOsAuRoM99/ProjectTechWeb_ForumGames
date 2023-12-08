
from django import forms
from .models import ComponentsComputer

class NewPC(forms.ModelForm): 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def savePC(self, request):
        c = ComponentsComputer()
        
        c.RAM = self.cleaned_data['RAM']
        c.CPU = self.cleaned_data['CPU']
        c.GPU = self.cleaned_data['GPU']
        c.MOBO = self.cleaned_data['MOBO']
        c.MEM = self.cleaned_data['MEM']
        c.PSU = self.cleaned_data['PSU']
        c.nickname = request.user
        c.PC_Photo = self.cleaned_data['PC_Photo']
        
        c.save()
        
    class Meta:
        model = ComponentsComputer
        exclude = ["Com_ID_num", "nickname"]
        labels={
            'CPU': '1. CPU',
            'GPU': '2. GPU',
            'RAM': '3. RAM',
            'MEM': '4. MEM',
            'PSU': '5. PSU',
            'MOBO': '6. MOBO',
            'PC_Photo': 'Aggiungi fotografia',
        }
        widgets = {
            'CPU': forms.Textarea(),
            'GPU': forms.Textarea(),
            'RAM': forms.Textarea(),
            'MEM': forms.Textarea(),
            'PSU': forms.Textarea(),
            'MOBO': forms.Textarea(),
        }
    