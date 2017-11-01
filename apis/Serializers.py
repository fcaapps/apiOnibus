from rest_framework import serializers
from .models import Produtos
from .models import Disciplina
from django.contrib.auth.models import User

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produtos
        fields = ('id', 'title', 'description', 'status', 'cost', 'price', 'created','owner')

class DisciplinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disciplina
        fields = ('id', 'title', 'description', 'professor')

class UserSerializer(serializers.ModelSerializer):
    produtos = serializers.PrimaryKeyRelatedField(many=True, queryset=Produtos.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'produtos')
