from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.views import APIView


from .serializers import NoteSerializer
from base.models import Note
from base.models import Empleado
from .serializers import EmpleadoSerializer
from base.models import Proyecto
from .serializers import ProyectoSerializer

from rest_framework.parsers import MultiPartParser, FormParser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
        'api/notes',
        'api/empleado'
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getEmpleado(request):
    user = request.user
    empleado = user.empleado_set.all()
    serializer = EmpleadoSerializer(empleado, many=True)
    return Response(serializer.data)

class ProyectoApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def post(self, request, *args, **kwargs):

        data = {
            'Codigo_CUI': request.data.get('Codigo_CUI'), 
            'Nombre': request.data.get('Nombre'), 
            'Codigo_SNIP':request.data.get('Codigo_SNIP'), 
            #'Foto_Perfil':request.data.get('Foto_Perfil'), 
            'Fecha_Registro':request.data.get('Fecha_Registro'), 
            'Fecha_Inicio': request.data.get('Fecha_Inicio'), 
            'Fecha_Fin': request.data.get('Fecha_Fin'), 
        }
        serializer = ProyectoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)