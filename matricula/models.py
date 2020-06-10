from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=200)

    def __str__(self):
            return self.rua

class Disciplina(models.Model):
    descricao = models.CharField(max_length=200)

    def __str__(self):
            return self.descricao

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    disciplinas = models.ManyToManyField(Disciplina)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    def __str__(self):
            return self.nome

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
            return self.disciplina