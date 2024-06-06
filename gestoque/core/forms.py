from django import forms
from .models import Categoria, Armazenamento, Marca, Unidade_Medida, Produto, Movimentacao_Estoque

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo_categoria']

class ArmazenamentoForm(forms.ModelForm):
    class Meta:
        model = Armazenamento
        fields = ['tipo_armazenamento']
    
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['marca']

class Unidade_MedidaForm(forms.ModelForm):
    class Meta:
        model = Unidade_Medida
        fields = ['unidade_medida']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao','categoria','armazenamento','estoque_minimo','unidade_medida','marca','estoque_atual']

class Movimentacao_EstoqueForm(forms.ModelForm):
    class Meta:
        model = Movimentacao_Estoque  # Usa o modelo Movimentacao_Estoque
        fields = ['produto', 'quantidade', 'tipo_movimentacao']  # Campos incluídos no formulário


