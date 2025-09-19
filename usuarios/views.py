from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from .forms import LoginForms, CadastroForms        

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form['senha1'].value() != form['senha2'].value():
                return redirect ('cadastro')
            
            nome=form['nome_login'].value()
            email=form['email'].value()
            senha=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
             
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            return redirect('login')

        
    return render(request, 'usuarios/cadastro.html', {'form': form})
