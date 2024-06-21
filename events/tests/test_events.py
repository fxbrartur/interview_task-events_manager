import pytest
from users.models import CustomUser
from rest_framework.test import APIClient
from events.models import Event


@pytest.mark.django_db
def test_create_event():
    user = CustomUser.objects.create_user(username='testuser', password='testpass')
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post('/api/events/', {
        'title': 'Test Event',
        'description': 'Event Description',
        'date': '2024-06-21',
        'time': '12:00:00',
        'location': 'Test Location'
    })
    assert response.status_code == 201
    assert Event.objects.count() == 1

@pytest.mark.django_db
def test_update_event():
    user = CustomUser.objects.create_user(username='testuser', password='testpass')
    event = Event.objects.create(
        title='Test Event',
        description='Event Description',
        date='2024-06-21',
        time='12:00:00',
        location='Test Location'
    )
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.patch(f'/api/events/{event.id}/', {
        'title': 'Updated Event'
    })
    assert response.status_code == 200
    event.refresh_from_db()
    assert event.title == 'Updated Event'

@pytest.mark.django_db
def test_delete_event():
    user = CustomUser.objects.create_user(username='testuser', password='testpass')
    event = Event.objects.create(
        title='Test Event',
        description='Event Description',
        date='2024-06-21',
        time='12:00:00',
        location='Test Location'
    )
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.delete(f'/api/events/{event.id}/')
    assert response.status_code == 204
    assert Event.objects.count() == 0
