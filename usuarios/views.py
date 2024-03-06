from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def novo_usuario(request):
    #tipo, validar, informar, salvar
    if request.method == 'POST':
        formulario =  UserRegisterForm(request.POST)
        if formulario.is_valid():
            #informar
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
            #salvar
    else:
        formulario = UserRegisterForm()

        
    return render(request, 'usuarios/registrar.html',{'formulario': formulario})

