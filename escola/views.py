from rest_framework import viewsets
from escola.models import Alunos,Funcionarios, Turmas,Etnia,TipoSanguinio, Sexo, Deficiente
from escola.serializer import AlunosSerializer, FuncionariosSerializer, TurmasSerializer,EtniaSerializer,TipoSanguinioSerializer,SexoSerializer,DeficienteSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer

class TurmasViewSet(viewsets.ModelViewSet):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer

class TipoSanguinioViewSet(viewsets.ModelViewSet):
    queryset = TipoSanguinio.objects.all()
    serializer_class = TipoSanguinioSerializer


class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer

class DeficienteViewSet(viewsets.ModelViewSet):
    queryset = Deficiente.objects.all()
    serializer_class = DeficienteSerializer