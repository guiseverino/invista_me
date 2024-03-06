from django.forms import ModelForm
from .models import Investimento

class InvestimentoForm(ModelForm):
    class Meta:
        #Classe que representa esse formlulario
        model = Investimento
        #campos a serem exibidos na tela
        fields = '__all__'