from django.shortcuts import render, redirect
from django import forms
from app_forms_cadastro.models import TabUsuarioCadastrados

class UsuariosCadatradosForm(forms.ModelForm):
  class Meta:
    model = TabUsuarioCadastrados
    fields = '__all__'
  
def cadastrar_usuario(request):
  if request.method == 'POST':
    form = UsuariosCadatradosForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("home") # incluir só uma vez no banco de dados
  else:
    form = UsuariosCadatradosForm() # formulario retorna vazio

  return render(request, "index.html", {"form": form})
