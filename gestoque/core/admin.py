#from django.contrib import admin
#from .models import Produto, Categoria, Armazenamento, Unidade_Medida, Marca, Movimentacao_Estoque

# admin.site.register(Produto)
# admin.site.register(Categoria)
# admin.site.register(Armazenamento)
# admin.site.register(Unidade_Medida)
# admin.site.register(Marca)
# admin.site.register(Movimentacao_Estoque)

# produtos/admin.py
from django.contrib import admin
from .models import Produto, Movimentacao_Estoque

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['descricao', 'categoria', 'armazenamento','estoque_atual']

@admin.register(Movimentacao_Estoque)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'tipo_movimentacao', 'data']
    list_filter = ['produto', 'tipo_movimentacao', 'data']