from django.db import models

class Categoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, null=False, blank=False, unique=True)
    def __str__(self):
        return self.tipo_categoria
    
class Armazenamento(models.Model):
    tipo_armazenamento = models.CharField(null=False, blank=False, max_length=50, unique=True)
    def __str__(self):
        return self.tipo_armazenamento
    
class Unidade_Medida(models.Model):
    unidade_medida = models.CharField(null=False, blank=False, max_length=15, unique=True)
    def __str__(self):
        return self.unidade_medida
    
class Marca(models.Model):
    marca = models.CharField(null=False, blank=False, max_length=50, unique=True)
    def __str__(self):
        return self.marca

class Produto(models.Model):
    descricao = models.CharField(null=False, blank=False, max_length=200, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, max_length=100)
    armazenamento = models.ForeignKey(Armazenamento, on_delete=models.CASCADE, max_length=30)
    unidade_medida = models.ForeignKey(Unidade_Medida, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE) 
    estoque_minimo = models.IntegerField(default=0)
    estoque_atual = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()  # Converte o nome para letras maiúsculas
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descricao

class Movimentacao_Estoque(models.Model):

    TIPO_MOVIMENTACAO_CHOICES = [
        ('entrada', 'Entrada'),  # Movimentação de entrada
        ('saida', 'Saída'),      # Movimentação de saída
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Produto relacionado à movimentação
    quantidade = models.IntegerField()  # Quantidade movimentada
    tipo_movimentacao = models.CharField(max_length=7, choices=TIPO_MOVIMENTACAO_CHOICES)
    data = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Ajusta o estoque do produto com base no tipo de movimentação
        if self.tipo_movimentacao == 'entrada':
            self.produto.estoque_atual += self.quantidade  # Incrementa o estoque
        elif self.tipo_movimentacao == 'saida':
            self.produto.estoque_atual -= self.quantidade  # Decrementa o estoque
        self.produto.save()  # Salva a atualização do produto
        super(Movimentacao_Estoque, self).save(*args, **kwargs)  # Chama o método save original

    def __str__(self):
        # Representação em string do objeto MovimentacaoEstoque
        return f'{self.tipo.capitalize()} de {self.quantidade} unidades de {self.produto.descricao}'
    

