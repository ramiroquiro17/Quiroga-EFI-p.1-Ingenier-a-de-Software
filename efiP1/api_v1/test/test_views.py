import pytest

from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APIClient

from factories import AutoFactory
from concesionaria.models import Auto
@pytest.mark.django_db
def test_list_autos(client: APIClient):
    auto_1 = AutoFactory()
    auto_2 = AutoFactory()

    url = reverse('autos-list')
    response = client.get(path=url)
    expected_result = [
  {
    "pk": auto_1.id,
    "marca": {
      "nombre": auto_1.marca.nombre
    },
    "modelo": {
      "nombre": auto_1.modelo.nombre
    },
    "categoria": {
      "nombre": auto_1.categoria.nombre
    },
    "color": {
      "nombre": auto_1.color.nombre
    },
    "pais": {
      "nombre": auto_1.pais.nombre
    },
    "numero_de_puertas": auto_1.numero_de_puertas,
    "cilindrada": f"{auto_1.cilindrada}",
    "tipo_de_combustible": auto_1.tipo_de_combustible,
    "precio": f"{auto_1.precio}"
  },
  {
     "pk": auto_2.id,
    "marca": {
      "nombre": auto_2.marca.nombre
    },
    "modelo": {
      "nombre": auto_2.modelo.nombre
    },
    "categoria": {
      "nombre": auto_2.categoria.nombre
    },
    "color": {
      "nombre": auto_2.color.nombre
    },
    "pais": {
      "nombre": auto_2.pais.nombre
    },
    "numero_de_puertas": auto_2.numero_de_puertas,
    "cilindrada": f"{auto_2.cilindrada}",
    "tipo_de_combustible": auto_2.tipo_de_combustible,
    "precio": f"{auto_2.precio}"
  },]
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db
def test_detail_autos(client: APIClient):
    auto_1 = AutoFactory()
    url = reverse('autos-detail', args=(auto_1.pk,))
    response = client.get(path=url)
    expected_result ={
    "pk": auto_1.id,
    "marca": {
      "nombre": auto_1.marca.nombre
    },
    "modelo": {
      "nombre": auto_1.modelo.nombre
    },
    "categoria": {
      "nombre": auto_1.categoria.nombre
    },
    "color": {
      "nombre": auto_1.color.nombre
    },
    "pais": {
      "nombre": auto_1.pais.nombre
    },
    "numero_de_puertas": auto_1.numero_de_puertas,
    "cilindrada": f"{auto_1.cilindrada}",
    "tipo_de_combustible": auto_1.tipo_de_combustible,
    "precio": f"{auto_1.precio}"
  }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

@pytest.mark.django_db
def test_delete_autos(client: APIClient):
    # Arrange
    auto_1 = AutoFactory()
    auto_2 = AutoFactory()
    auto_3 = AutoFactory()
    auto_4 = AutoFactory()
    # Act
    url = reverse('autos-detail', args=(auto_2.pk,))
    response = client.delete(path=url)

    autos = Auto.objects.all()
    assert autos.count() == 3
    assert auto_2 not in autos

