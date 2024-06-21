import pytest
from rest_framework.test import APIClient
from users.models import CustomUser
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_create_user():
    client = APIClient()
    response = client.post('/api/users/', {
        'username': 'testuser',
        'password': 'testpass',
        'email': 'test@example.com'
    })
    assert response.status_code == 201
    assert CustomUser.objects.count() == 1

@pytest.mark.django_db
def test_update_user():
    user = CustomUser.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    Token.objects.create(user=user) 
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(f'/api/users/{user.id}/', {
        'username': 'testuser',
        'first_name': 'Test',
        'last_name': user.last_name,
        'email': user.email,
        'password': 'testpass' 
    })
    assert response.status_code == 200
    user.refresh_from_db()
    assert user.first_name == 'Test'

@pytest.mark.django_db
def test_delete_user():
    user = CustomUser.objects.create_user(username='testuser', password='testpass')
    Token.objects.create(user=user)  
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.delete(f'/api/users/{user.id}/')
    assert response.status_code == 204
    assert CustomUser.objects.count() == 0
