from rest_framework import viewsets
from escola.models import Alunos,Funcionarios, Turmas,Etnia,TipoSanguinio, Sexo, Deficiente
from escola.serializer import UserSerializer,AlunosSerializer, FuncionariosSerializer, TurmasSerializer,EtniaSerializer,TipoSanguinioSerializer,SexoSerializer,DeficienteSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response({"error": "Login ou senha inválidos"}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data})



@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add a custom route for password update
    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        password = request.data.get('password')
        if password is not None:
            user.set_password(password)
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response({'error': 'Password is not provided'}, status=status.HTTP_400_BAD_REQUEST)
@permission_classes([IsAuthenticated])
class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer

@permission_classes([IsAuthenticated])
class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer

@permission_classes([IsAuthenticated])
class TurmasViewSet(viewsets.ModelViewSet):
    queryset = Turmas.objects.all()
    serializer_class = TurmasSerializer

@permission_classes([IsAuthenticated])
class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer

@permission_classes([IsAuthenticated])
class TipoSanguinioViewSet(viewsets.ModelViewSet):
    queryset = TipoSanguinio.objects.all()
    serializer_class = TipoSanguinioSerializer

@permission_classes([IsAuthenticated])
class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer

@permission_classes([IsAuthenticated])
class DeficienteViewSet(viewsets.ModelViewSet):
    queryset = Deficiente.objects.all()
    serializer_class = DeficienteSerializer




class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)