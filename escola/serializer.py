from rest_framework import serializers
from escola.models import *


class AnoEscolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnoEscolar
        fields = ['id', 'serie_escolar']


class AlergicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergico
        fields = ['id', 'alergia']


class DeficienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deficiente
        fields = ['id', 'deficiencia']


class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = ['id', 'celular', 'telefone', 'email']


class EtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etnia
        fields = ['id', 'etnia']


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = ['id', 'sexo']


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'turno']


class TipoSanguinioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSanguinio
        fields = ['id', 'tipo']


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'logradouro', 'numero', 'completo', 'ponto_refrencia']


class AlunosSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    alergico = AlergicoSerializer()
    deficiente = DeficienteSerializer()
    contato = ContatosSerializer()
    sexo = SexoSerializer()
    etinia = EtniaSerializer()
    ano_escolar = AnoEscolarSerializer()
    turno = TurnoSerializer()
    tipo_sanguinio = TipoSanguinioSerializer()

    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'nome_pai', 'nome_mae', 'endereco', 'naturalidade', 'alergico', 'deficiente', 'contato', 'sexo', 'etinia', 'ano_escolar', 'turno', 'tipo_sanguinio', 'user_type', 'created_at', 'updated_at']


class TurmasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turmas
        fields = ['id', 'nome','sala','turno']


class AlunosTurmaSerializer(serializers.ModelSerializer):
    turmas_id = TurmasSerializer()
    aluno_id = AlunosSerializer()

    class Meta:
        model = AlunosTurma
        fields = ['id', 'turmas_id', 'aluno_id']


class DiciplinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diciplinas
        fields = ['id', 'diciplinas']


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = ['id', 'cargo', 'funcao']


class FuncionariosSerializer(serializers.ModelSerializer):
    contato = ContatosSerializer()
    endereco = EnderecoSerializer()
    sexo = SexoSerializer()
    etinia = EtniaSerializer()
    funcao = FuncaoSerializer()

    class Meta:
        model = Funcionarios
        fields = ['id', 'nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'naturalidade', 'contato', 'endereco', 'sexo', 'etinia', 'funcao', 'user_type', 'created_at', 'updated_at']


class TurmaFuncionarioSerializer(serializers.ModelSerializer):
    turma_id = TurmasSerializer()
    funcionario_id = FuncionariosSerializer()

    class Meta:
        model = TurmaFuncionario
        fields = ['id', 'turma_id', 'funcionario_id']


class TurmaEscolarSerializer(serializers.ModelSerializer):
    funcionario_turma = TurmaFuncionarioSerializer()
    serie_escolar = AnoEscolarSerializer()
    turno = TurnoSerializer()
    diciplina = DiciplinasSerializer()

    class Meta:
        model = TurmaEscolar
        fields = ['id', 'funcionario_turma', 'serie_escolar', 'turno', 'diciplina']


class ResponsavelSerializer(serializers.ModelSerializer):
    contato = ContatosSerializer()
    endereco = EnderecoSerializer()
    sexo = SexoSerializer()
    etinia = EtniaSerializer()

    class Meta:
        model = Responsavel
        fields = ['id', 'nome', 'sobrenome', 'nascimento', 'rg', 'cpf', 'naturalidade', 'contato', 'endereco', 'sexo', 'etinia', 'user_type', 'created_at', 'updated_at']


class ResponsavelAlunosSerializer(serializers.ModelSerializer):
    responsavel_id = ResponsavelSerializer()
    alunos_id = AlunosSerializer()

    class Meta:
        model = ResponsavelAlunos
        fields = ['id', 'responsavel_id', 'alunos_id']
