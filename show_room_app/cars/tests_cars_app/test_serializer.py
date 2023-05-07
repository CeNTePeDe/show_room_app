import pytest
from django.urls import reverse
from rest_framework import status

from cars.models import Car
from cars.serializer import CarSerializer

@pytest.mark.django_db
def test_car_list(client):
    url = reverse('car-list')
    response = client.get(url)
    car = Car.objects.all()
    expected_data = CarSerializer(car, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data


@pytest.mark.django_db
def test_create_car(api_client, car_payload):
    url = '/api/v1_car/cars/'

    response = api_client.post(url, car_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert Car.objects.count() == 1


@pytest.mark.django_db
def test_get_car(api_client, create_car):
    response = api_client.get(reverse('car-list'))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

    car_data = dict(response.data[0])
    assert car_data['name'] == create_car.name
    assert car_data['model_car'] == create_car.model_car
    assert car_data['year'] == int(create_car.year)
    assert car_data['country'] == create_car.country
    assert car_data['body_type'] == create_car.body_type
    assert car_data['color'] == create_car.color
    assert car_data['engine_type'] == create_car.engine_type
    assert car_data['number_of_doors'] == create_car.number_of_doors
    assert car_data['is_active'] == create_car.is_active





