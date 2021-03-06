from rest_framework import serializers
from .models import cursos, aulas, User2

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User2
        fields = '__all__'

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = cursos
        fields = '__all__'

class CursosAlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = cursos
        fields = ('id', 'Nome', 'descricao','categoria', 'professores', 'datadepublicacao', 'datadeedicao')

class Cursosalunosid(serializers.ModelSerializer):
    class Meta:
        model = cursos
        fields = ("usuarios", )

class AulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = aulas
        fields = '__all__'