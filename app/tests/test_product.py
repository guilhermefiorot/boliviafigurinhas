import json
import uuid
from flask import url_for
from app.models.product import Product
from app.services.user_service import create_user


def create_test_user(session):
    """Creates a unique test user to avoid UNIQUE constraint failures."""
    user_data = {
        'name': 'testuser',
        'email': 'testuser2@example.com',
        'password': 'testpassword',
        'endereco': 'Rua 1, 123',
        'cidade': 'Espirito Santo',
        'cep': '29100000',
        'pais': 'Brasil',
        'telefone': '27999999999',
        'cpf': '01234567890',
    }
    user = create_user(user_data)
    session.commit()
    return user


def create_test_product(session):
    """Creates a test product with required fields to prevent NULL errors."""
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
    """Obtains a valid access token for authentication."""
    response = client.post(
        url_for('api.loginresource'),
        json={'email': email, 'password': password}
    )
    assert response.status_code == 200, "Failed to obtain authentication token"
    return response.get_json()['access_token']


def test_add_product(client, session):
    """Tests adding a new product to the database."""
    user = create_test_user(session)
    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product_data = {
        'name': 'New Product',
        'description': 'A new test product.',
        'image': 'https://example.com/newproduct.jpg',
        'price': 150.0,
        'condition': 8.0,
        'rarity': 'Common',
        'quantity': 20
    }

    response = client.post(
        url_for('api.productlistresource'),
        json=product_data,
        headers=headers
    )

    assert response.status_code == 201, f"Unexpected response: {response.get_json()}"
    data = response.get_json()
    assert data['name'] == product_data['name']



def test_get_product(client, session):
    """Tests retrieving a product from the database."""
    user = create_test_user(session)
    access_token = get_access_token(client, user.email, 'testpassword')
    headers = {'Authorization': f'Bearer {access_token}'}

    product = create_test_product(session)

    response = client.get(url_for('api.productresource', id=product.id), headers=headers)
    assert response.status_code == 200, f"Unexpected response: {response.get_json()}"

    data = response.get_json()
    assert data['name'] == product.name
