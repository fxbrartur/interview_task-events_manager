import pytest
from django.contrib.auth import get_user_model
from events.models import Event
from events.tasks import send_event_update_notification, send_subscription_confirmation


User = get_user_model()

@pytest.mark.django_db
def test_send_event_update_notification(capfd):
    event = Event.objects.create(
        title='Test Event',
        description='Event Description',
        date='2024-06-21',
        time='12:00:00',
        location='Test Location'
    )
    send_event_update_notification(event.id)
    captured = capfd.readouterr()
    assert f"Event '{event.title}' has been updated." in captured.out

@pytest.mark.django_db
def test_send_subscription_confirmation(capfd):
    user = User.objects.create_user(username='testuser', password='testpass', email='test@example.com')
    event = Event.objects.create(
        title='Test Event',
        description='Event Description',
        date='2024-06-21',
        time='12:00:00',
        location='Test Location'
    )
    send_subscription_confirmation(event.id, user.id)
    captured = capfd.readouterr()
    assert f"User '{user.username}' has subscribed to event '{event.title}'." in captured.out