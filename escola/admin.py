from django.contrib import admin
from escola.models import AnoEscolar, Alergico, Deficiente, Contatos, Etnia, Sexo, Turno, TipoSanguinio, Endereco, Alunos, Turmas, AlunosTurma, Diciplinas, Funcao, Funcionarios, TurmaFuncionario, TurmaEscolar, Responsavel, ResponsavelAlunos

class AlunosTurmaInline(admin.TabularInline):
    model = AlunosTurma

class TurmaFuncionarioInline(admin.TabularInline):
    model = TurmaFuncionario

class ResponsavelAlunosInline(admin.TabularInline):
    model = ResponsavelAlunos

@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    inlines = (AlunosTurmaInline, ResponsavelAlunosInline)
    list_display = ('nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'user_type', 'created_at', 'updated_at')

@admin.register(AnoEscolar, Alergico, Deficiente, Etnia, Sexo, Turno, TipoSanguinio, Diciplinas, Funcao)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ('__str__',)

@admin.register(Turmas)
class TurmasAdmin(admin.ModelAdmin):
    inlines = (AlunosTurmaInline, TurmaFuncionarioInline)
    list_display = ('nome','sala','turno')
    

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    inlines = (TurmaFuncionarioInline,)
    list_display = ('nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'user_type', 'created_at', 'updated_at')

@admin.register(TurmaEscolar)
class TurmaEscolarAdmin(admin.ModelAdmin):
    list_display = ('funcionario_turma', 'serie_escolar', 'turno', 'diciplina')

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    inlines = (ResponsavelAlunosInline,)
    list_display = ('nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'user_type', 'created_at', 'updated_at')

@admin.register(AlunosTurma)
class AlunosTurmaAdmin(admin.ModelAdmin):
    list_display = ('turmas_id', 'aluno_id')

@admin.register(ResponsavelAlunos)
class ResponsavelAlunosAdmin(admin.ModelAdmin):
    list_display = ('responsavel_id', 'alunos_id')

# Registrando os modelos que foram deixados de fora
@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'numero', 'cep')

@admin.register(Contatos)
class ContatosAdmin(admin.ModelAdmin):
    list_display = ('celular', 'telefone', 'email')
