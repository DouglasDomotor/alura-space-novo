from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .forms import LoginForms, CadastroForms   

from django.contrib import auth

from django.contrib import messages


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')
    
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha1'].value() != form['senha2'].value():
                messages.error(request, 'Senhas não são iguais')
                return redirect ('cadastro')
            
            nome=form['nome_login'].value()
            email=form['email'].value()
            senha=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
        else:
            messages.error(request, 'Formulario inválido')

        
    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login')
