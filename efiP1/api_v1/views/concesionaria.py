import csv
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import action
from api_v1.serializers.concesionaria_serializers import AutoSerializer, ComentarioSerializer, SedeSerializer, ProveedorSerializer, UserSerializer
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from api_v1.filters import AutoFilter
from concesionaria.models import Auto, Comentario, Sede, Proveedor, Categoria, Marca, Modelo, Color, Pais, Ciudad
from django.contrib.auth.models import User
from rest_framework import status

class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['marca__nombre','modelo__nombre','categoria__nombre','color__nombre','pais__nombre']
    filterset_class = AutoFilter

    def create(self, request, *args, **kwargs):
        data = request.data

        def get_or_create_relation(model, field_name):
            relation_data = data.get(field_name)
            if relation_data and isinstance(relation_data, dict):
                name = relation_data.get('nombre')
                return model.objects.get_or_create(nombre=name)[0]
            return None

        marca = get_or_create_relation(Marca, 'marca')
        modelo = get_or_create_relation(Modelo, 'modelo')
        categoria = get_or_create_relation(Categoria, 'categoria')
        color = get_or_create_relation(Color, 'color')
        pais = get_or_create_relation(Pais, 'pais')

        auto = Auto.objects.create(
            marca=marca,
            modelo=modelo,
            categoria=categoria,
            color=color,
            pais=pais,
            numero_de_puertas=data.get('numero_de_puertas'),
            cilindrada=data.get('cilindrada'),
            tipo_de_combustible=data.get('tipo_de_combustible'),
            precio=data.get('precio')
        )

        serializer = self.serializer_class(auto)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        def get_or_create_relation(model, field_name):
            relation_data = data.get(field_name)
            if relation_data and isinstance(relation_data, dict):
                name = relation_data.get('nombre')
                return model.objects.get_or_create(nombre=name)[0]
            return None

        marca = get_or_create_relation(Marca, 'marca') or instance.marca
        modelo = get_or_create_relation(Modelo, 'modelo') or instance.modelo
        categoria = get_or_create_relation(Categoria, 'categoria') or instance.categoria
        color = get_or_create_relation(Color, 'color') or instance.color
        pais = get_or_create_relation(Pais, 'pais') or instance.pais

        instance.marca = marca
        instance.modelo = modelo
        instance.categoria = categoria
        instance.color = color
        instance.pais = pais
        instance.numero_de_puertas = data.get('numero_de_puertas', instance.numero_de_puertas)
        instance.cilindrada = data.get('cilindrada', instance.cilindrada)
        instance.tipo_de_combustible = data.get('tipo_de_combustible', instance.tipo_de_combustible)
        instance.precio = data.get('precio', instance.precio)

        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail= False, url_path='download-csv')
    def download_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="autos.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                'pk','marca','modelo','categoria','color','pais','numero_de_puertas','cilindrada','tipo_de_combustible','precio'
            ]
        )
        autos = self.get_queryset()
        

        for auto in autos:
            writer.writerow(
            [
                auto.pk,
                auto.marca.nombre,
                auto.modelo.nombre, 
                auto.categoria.nombre, 
                auto.color.nombre, 
                auto.pais.nombre,
                auto.numero_de_puertas,
                auto.cilindrada,
                auto.tipo_de_combustible
            ]
        )
        return response
    
    @action(methods=['get'], detail=False, url_path='latest')
    def last_auto(self, request):
        last_auto = self.get_queryset().last()
        serializer = self.serializer_class(last_auto)
        return Response(serializer.data)


class ComentariosPorAuto(APIView):
    def get(self, request, auto_id):
        comentarios = Comentario.objects.filter(auto_id=auto_id)
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SedeViewSet(ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer

    def create(self, request, *args, **kwargs):
        data = request.data

        ciudad_data = data.get('ciudad')
        ciudad = None
        if ciudad_data and isinstance(ciudad_data, dict):
            ciudad_nombre = ciudad_data.get('nombre')
            ciudad, created = Ciudad.objects.get_or_create(nombre=ciudad_nombre)

        sede = Sede.objects.create(
            nombre=data.get('nombre'),
            ciudad_id=ciudad,
            gerente=data.get('gerente'),
            direccion=data.get('direccion'),
            telefono=data.get('telefono')
        )
        serializer = self.serializer_class(sede)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProveedorViewSet(ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Extraer datos de la solicitud
        data = request.data

        # Crear el usuario
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        
        # Configurar la contraseña hasheada
        password = data.get('password')
        if password:
            user.set_password(password)  # Hashea la contraseña
        else:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Guardar el usuario
        user.save()

        # Serializar y devolver el usuario creado
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)