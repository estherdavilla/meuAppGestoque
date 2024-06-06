from core.models import Categoria

# Tente buscar o produto com id 1
try:
    tipo_categoria = Categoria.objects.get(id=1)
    tipo_categoria.delete()
    print("Produto excluído com sucesso.")
except Categoria.DoesNotExist:
    print("Produto não encontrado.")
