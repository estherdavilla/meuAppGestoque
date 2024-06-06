from django.urls import path
from .views import lista_produtos, movimentacao_estoque, admin_index, produto_create, produto_update, produto_delete, login_view, logout_view, register_view, cadastroCategoria_view, cadastroArmazenamento_view, cadastroMarca_view, cadastroUnidadeMedida_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('home', admin_index, name='index'),
    path('produto/lista', lista_produtos, name='lista_produtos'),
    path('produto/novo/', produto_create, name='criar_produto'),
    path('cadastro/categoria', cadastroCategoria_view, name='cadastroCategoria'),
    path('cadastro/armazenamento', cadastroArmazenamento_view, name='cadastroArmazenamento'),
    path('cadastro/marca', cadastroMarca_view, name='cadastroMarca'),
    path('cadastro/unidadeMed', cadastroUnidadeMedida_view, name='cadastroUniMed'),
    path('produto/<int:pk>/editar/', produto_update, name='editar_produto'),
    path('produto/<int:pk>/excluir/', produto_delete, name='excluir_produto'),
    path('estoque/', movimentacao_estoque, name='movimentacao_estoque'),
]

# urlpatterns = [
#     path('', admin_index, name='index'),
#     path('produtos/', lista_produtos, name='lista_produtos'),  # URL para a lista de produtos
#     path('movimentacao/', movimentacao_estoque, name='movimentacao_estoque'),  # URL para registrar movimentação de estoque
# ]
