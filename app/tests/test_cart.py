import math
import json
from flask import url_for
from app.models.product import Product
from app.services.user_service import create_user


def create_test_user(session):
    user_data = {
        'name': 'testuser',
        'email': 'testuser1@example.com',
        'password': 'testpassword',
        'endereco': 'Rua 1, 123',
        'cidade': 'Espirito Santo',
        'cep': '29100000',
        'pais': 'Brasil',
        'telefone': '27999999999',
        'cpf': '00987654321',
    }
    user = create_user(user_data)
    session.commit()
    return user


def create_test_product(session):
    product_data = {
        'name': 'Test Product',
        'description': 'This is a test product.',
        'image': 'https://example.com/product.jpg',
        'price': 100.0,
        'condition': 9.5,
        'rarity': 'Rare',
        'quantity': 10
    }
    product = Product(**product_data)
    session.add(product)
    session.commit()
    return product


def get_access_token(client, email, password):
    response = client.post(
        url_for('api.loginresource'),
        json={'email': email, 'password': password}
    )
    assert response.status_code == 200, f"Login failed: {response.get_json()}"
    data = response.get_json()
    assert 'access_token' in data, f"Unexpected response: {data}"
    return data['access_token']


def test_add_item_to_cart(client, session):
    user = create_test_user(session)

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product = create_test_product(session)

    response = client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )
    assert response.status_code == 201, f"Unexpected response: {response.status_code}, Data: {response.get_json()}"
    data = response.get_json()
    assert data['product_id'] == product.id
    assert data['quantity'] == 2


def test_get_cart(client, session):
    user = create_test_user(session)

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product = create_test_product(session)

    client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )

    response = client.get(url_for('api.cartresource'), headers=headers)
    assert response.status_code == 200, f"Unexpected response: {response.status_code}, Data: {response.get_json()}"
    data = response.get_json()
    assert len(data['items']) == 1
    assert data['items'][0]['product_id'] == product.id
    assert data['items'][0]['quantity'] == 2
    assert math.isclose(data['total_value'], product.price * 2)


def test_remove_item_from_cart(client, session):
    user = create_test_user(session)

    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product = create_test_product(session)

    client.post(
        url_for('api.cartresource'),
        json={'product_id': product.id, 'quantity': 2},
        headers=headers
    )

    response = client.delete(
        url_for('api.cartresource'),
        json={'product_id': product.id},
        headers=headers
    )
    assert response.status_code == 204, f"Unexpected response: {response.status_code}"
    response = client.get(url_for('api.cartresource'), headers=headers)
    data = response.get_json()
    assert len(data['items']) == 0
    assert math.isclose(data['total_value'], 0.0)
