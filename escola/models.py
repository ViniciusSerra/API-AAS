
from django.db import models



class AnoEscolar (models.Model):
    serie_escolar = models.CharField(max_length=30) 
    def __str__(self):
        return self.serie_escolar



class Alergico(models.Model):
    alergia = models.CharField(max_length=255)

    def __str__(self):
        return self.alergia



class Deficiente(models.Model):
    deficiencia = models.CharField(max_length=30)

    def __str__(self):
        return self.deficiencia




class Contatos(models.Model):
    celular = models.CharField(max_length=12)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return f'{self.celular}, {self.telefone}, {self.email}'




class Etnia(models.Model):
    etnia = models.CharField(max_length=30)
    def __str__(self):
        return self.etnia



class Sexo(models.Model):
    sexo = models.CharField(max_length=20)

    def __str__(self):
        return self.sexo



class Turno(models.Model):
    turno = models.CharField(max_length=30)

    def __str__(self):
        return self.turno


class TipoSanguinio(models.Model):
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.tipo

class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=30) 
    numero = models.CharField(max_length=6)
    completo = models.CharField(max_length=255)
    ponto_refrencia = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.logradouro}, {self.numero}, {self.completo}'

class Alunos(models.Model):
    nome= models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11) 
    nome_pai = models.CharField(max_length=100)
    nome_mae = models.CharField(max_length=100)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    naturalidade = models.CharField(max_length=100)
    alergico = models.ForeignKey(Alergico, on_delete=models.PROTECT)
    deficiente = models.ForeignKey(Deficiente, on_delete=models.PROTECT)
    contato = models.ForeignKey(Contatos, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    etinia = models.ForeignKey(Etnia, on_delete=models.PROTECT)
    ano_escolar = models.ForeignKey(AnoEscolar,on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    tipo_sanguinio = models.ForeignKey(TipoSanguinio, on_delete=models.PROTECT)
    user_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
    
class Turmas(models.Model):
    nome = models.CharField(max_length=30)
    sala = models.CharField(max_length=10)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class AlunosTurma(models.Model):
    turmas_id = models.ForeignKey(Turmas, on_delete=models.PROTECT)
    aluno_id = models.ForeignKey(Alunos, on_delete=models.PROTECT)

    def __str__(self):
        return f'Turma: {self.turmas_id.nome}, Aluno: {self.aluno_id.nome}'



class Diciplinas(models.Model):
    diciplinas = models.CharField(max_length=11) 


class Funcao(models.Model):
    cargo = models.CharField(max_length=30)
    funcao = models.CharField(max_length=255)

class Funcionarios(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11) 
    naturalidade = models.CharField(max_length=100)
    contato = models.ForeignKey(Contatos, on_delete=models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    etinia = models.ForeignKey(Etnia, on_delete=models.PROTECT)
    funcao = models.ForeignKey(Funcao, on_delete=models.PROTECT)
    user_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome


class TurmaFuncionario(models.Model):
    turma_id = models.ForeignKey(Turmas, on_delete=models.PROTECT)
    funcionario_id = models.ForeignKey(Funcionarios, on_delete=models.PROTECT)


class TurmaEscolar(models.Model):
    funcionario_turma = models.ForeignKey(TurmaFuncionario, on_delete=models.PROTECT)
    serie_escolar = models.ForeignKey(AnoEscolar, on_delete=models.PROTECT)
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    diciplina = models.ForeignKey(Diciplinas, on_delete=models.PROTECT)
    def __str__(self):
      return f'Turma: {self.turma_id.nome}, Funcionário: {self.funcionario_id.nome}'





class Responsavel(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    nascimento = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11) 
    naturalidade = models.CharField(max_length=100)
    contato = models.ForeignKey(Contatos, on_delete=models.PROTECT)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    sexo = models.ForeignKey(Sexo, on_delete=models.PROTECT)
    etinia = models.ForeignKey(Etnia, on_delete=models.PROTECT)
    user_type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Responsável: {self.nome}'

class ResponsavelAlunos(models.Model):
    responsavel_id = models.ForeignKey(Responsavel, on_delete=models.PROTECT)
    alunos_id = models.ForeignKey(Alunos, on_delete=models.PROTECT)
    def __str__(self):
        return f'Responsável: {self.responsavel_id.nome}, Aluno: {self.alunos_id.nome}'
