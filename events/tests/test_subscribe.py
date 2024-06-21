import pytest
from users.models import CustomUser
from rest_framework.test import APIClient
from events.models import Event


@pytest.mark.django_db
def test_register_participant():
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
    response = client.post(f'/api/events/{event.id}/subscribe/')
    assert response.status_code == 200
    assert user in event.participants.all()
