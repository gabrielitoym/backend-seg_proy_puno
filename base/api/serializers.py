from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Note
from base.models import Empleado
from base.models import Proyecto

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class EmpleadoSerializer(ModelSerializer):
    creator_id = serializers.ReadOnlyField(source='user.id')
    creator = serializers.ReadOnlyField(source='user.username')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Empleado
        fields = '__all__'

class ProyectoSerializer(ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Proyecto
        fields = '__all__'
