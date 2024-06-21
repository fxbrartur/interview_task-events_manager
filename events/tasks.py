from celery import shared_task
from events.models import Event
from users.models import CustomUser


@shared_task
def send_event_update_notification(event_id):
    try:
        event = Event.objects.get(id=event_id)
        print(f"Event '{event.title}' has been updated. Details: {event.description}, Date: {event.date}, Time: {event.time}, Location: {event.location}")
    except Event.DoesNotExist:
        print(f"Event with id {event_id} does not exist.")

@shared_task
def send_subscription_confirmation(event_id, user_id):
    try:
        event = Event.objects.get(id=event_id)
        user = CustomUser.objects.get(id=user_id)
        print(f"User '{user.username}' has subscribed to event '{event.title}'.")
    except (Event.DoesNotExist, CustomUser.DoesNotExist) as e:
        print(str(e))

@shared_task
def generate_event_report(event_id):
    try:
        event = Event.objects.get(id=event_id)
        participants = event.participants.values('first_name', 'last_name', 'email', 'image')
        report = {
            'event': event.title,
            'participant_count': event.participants.count(),
            'participants': list(participants)
        }
        print(f"Generated report for event '{event.title}': {report}")
        return report
    except Event.DoesNotExist:
        print(f"Event with id {event_id} does not exist.")
        return None
            