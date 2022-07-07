from app_Matriculas.models import Matricula
from rest_framework import serializer
from .models import *

class MatriculaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class AlumnoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'