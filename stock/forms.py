from django import forms
from .models import Estoque, EstoqueItens
from plataform.models import Item, Partner
from activation.models import TokenUser, Company



class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Estoque
        fields = ('tipo_registro', 'status', 'partner', 'nf', 'company')

    def __init__(self, user=None, *args, **kwargs):
        super(EstoqueForm, self).__init__(*args, **kwargs)
        if user.is_authenticated:
            user_company_value = TokenUser.objects.filter(user=user).values('company_id')
            self.company = user_company_value[0]['company_id']
            self.fields['partner'].queryset = Partner.objects.filter(company_id=self.company)
            self.fields['company'].queryset = Company.objects.filter(id=self.company)



class EstoqueItensEntradaForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'


class EstoqueItensSaidaForm(forms.ModelForm):

    class Meta:
        model = EstoqueItens
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(EstoqueItensSaidaForm, self).__init__(*args, **kwargs)
        # Retorna somente produtos com estoque maior do que zero.
        self.fields['produto'].queryset = Item.objects.filter(stock_qtd__gt=0)
