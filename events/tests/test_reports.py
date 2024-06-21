import pytest
from users.models import CustomUser
from events.models import Event
from events.views import generate_event_report


@pytest.mark.django_db
def test_generate_report():
    event = Event.objects.create(
        title='Test Event',
        description='Event Description',
        date='2024-06-21',
        time='12:00:00',
        location='Test Location'
    )
    user1 = CustomUser.objects.create_user(username='testuser1', password='testpass', email='user@example.com', first_name='Test', last_name='User')
    user2 = CustomUser.objects.create_user(username='testuser2', password='testpass', email='user2@example.com', first_name='Test2', last_name='User2')
    event.participants.add(user1, user2)

    report = generate_event_report(event.id)
    assert len(report['participants']) == 2
    assert report['participants'][0]['first_name'] == 'Test'
    assert report['participants'][1]['first_name'] == 'Test2'
