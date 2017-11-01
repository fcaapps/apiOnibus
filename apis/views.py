from django.shortcuts import render

from .models import Produtos
from .models import Disciplina
from rest_framework import viewsets
from .Serializers import ProdutoSerializer, DisciplinaSerializer, UserSerializer
from django.contrib.auth.models import User

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all().order_by('-created')
    serializer_class = ProdutoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all().order_by('-created')
    serializer_class = DisciplinaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
