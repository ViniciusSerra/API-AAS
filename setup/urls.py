
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet,UserViewSet,FuncionarioViewSet,TurmasViewSet,EtniaViewSet,TipoSanguinioViewSet,SexoViewSet, DeficienteViewSet, LoginView,LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet,basename='alunos')
router.register('funcionario',FuncionarioViewSet,basename='funcionario')
router.register('Turmas',TurmasViewSet,basename='turmas')
router.register('etnia',EtniaViewSet,basename='etnia')
router.register('TipoSanguinio',TipoSanguinioViewSet,basename='TipoSanguinio')
router.register('sexo',SexoViewSet,basename='sexo')
router.register('deficiencias',DeficienteViewSet,basename='deficiencias')
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]