from rest_framework import viewset
from .serializer import *
from .models import Matricula, Alumno

class MatriculaViewset(viewset.ModelViewset):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class AlumnoViewset(viewset.ModelViewset):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer