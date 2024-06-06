from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produto, Movimentacao_Estoque
from .forms import Movimentacao_EstoqueForm, ProdutoForm, CategoriaForm, ArmazenamentoForm, MarcaForm, Unidade_MedidaForm

def admin_index(request):
    return render(request, 'index.html')

# View para listar todos os produtos
def lista_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'lista_produtos.html', {'produtos': produtos})  # Renderiza o template com a lista de produtos

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'criar_produto.html', {'form': form})

def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'excluir_produto.html', {'produto': produto})

def movimentacao_estoque(request):
    if request.method == 'POST':
        form = Movimentacao_EstoqueForm(request.POST)  # Formulário preenchido pelo usuário
        if form.is_valid():
            form.save()  # Salva a movimentação se o formulário for válido
            return redirect('lista_produtos')  # Redireciona para a lista de produtos
    else:
        form = Movimentacao_EstoqueForm()  # Formulário vazio para uma nova movimentação
    return render(request, 'movimentacao_estoque.html', {'form': form})  # Renderiza o template com o formulário

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_produtos')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'cadastro/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso. Você já pode fazer login!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro/register.html', {'form': form})

def cadastroCategoria_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação se o formulário for válido
            return redirect('criar_produto')
    else:
        form = CategoriaForm()  # Formulário vazio para uma nova movimentação
    return render(request, 'cadastroCategoria.html', {'form': form})

def cadastroArmazenamento_view(request):
    if request.method == 'POST':
        form = ArmazenamentoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação se o formulário for válido
            return redirect('criar_produto')
    else:
        form = ArmazenamentoForm()  # Formulário vazio para uma nova movimentação
    return render(request, 'cadastroArmazenamento.html', {'form': form})

def cadastroMarca_view(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação se o formulário for válido
            return redirect('criar_produto')
    else:
        form = MarcaForm()  # Formulário vazio para uma nova movimentação
    return render(request, 'cadastroMarca.html', {'form': form})

def cadastroUnidadeMedida_view(request):
    if request.method == 'POST':
        form = Unidade_MedidaForm(request.POST)
        if form.is_valid():
            form.save()  # Salva a movimentação se o formulário for válido
            return redirect('criar_produto')
    else:
        form = Unidade_MedidaForm()  # Formulário vazio para uma nova movimentação
    return render(request, 'cadastroUniMed.html', {'form': form})

