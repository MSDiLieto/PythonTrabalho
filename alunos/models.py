from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    observacoes = models.TextField(null=True, blank=True)


