from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        #você pode segmentar os campos que vão aparecer aqui 
        fields = '__all__'


