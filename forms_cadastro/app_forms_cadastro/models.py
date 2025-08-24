from django.db import models

class TabUsuarioCadastrados(models.Model):
  nome = models.CharField(max_length=255)
  endereco = models.CharField(max_length=255)
  idade = models.PositiveIntegerField()
  dt_nascimento = models.DateField()
  raca_choices = [
    ("preto", "Preto"),
    ("amarelo", "Amarelo"),
    ("branco", "Branco"),
    ("pardo", "Pardo"),
  ]
  raca = models.CharField(max_length=15, choices=raca_choices)
  formacao_choices = [
    ("medio_incompleto", "Ensino Médio Incompleto"),
    ("medio_completo", "Ensino Médio Completo"),
    ("superior_incompleto", "Superior Incompleto"),
    ("superior_completo", "Superior Completo"),
    ("curso_tecnico", "Curso Técnico"),
    ("pos_graduacao", "Pós Gradução"),
  ]
  formacao = models.CharField(max_length=180, choices=formacao_choices)
  arquivo = models.FileField(upload_to='arquivos/', null=True)
  
  def __str__(self):
    return self.nome
  
  class Meta:
    db_table = "[DJANGO].[TAB_USUARIOS_CADASTRADOS]"
    