#importar los modelos
from .models import Facultad, Programa, Docente

##importar los serializers
from .serializers import FacultadSerializer, ProgramaSerializer, DocenteSerializer

##imports para trabajar con django rest framework
from rest_framework import viewsets


##vistas del rest_framework
class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all().order_by('-pub_date')
    serializer_class = FacultadSerializer
    
class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all().order_by('-pub_date')
    serializer_class = ProgramaSerializer
    
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all().order_by('-pub_date')
    serializer_class = DocenteSerializer
    