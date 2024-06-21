from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from events.models import Event
from events.serializers import EventSerializer
from users.models import CustomUser
from .tasks import send_event_update_notification, send_subscription_confirmation, generate_event_report
from drf_spectacular.utils import extend_schema, extend_schema_view



@extend_schema_view(
    partial_update=extend_schema(exclude=True),
    subscribe=extend_schema(request=None)
)
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        send_event_update_notification.delay(kwargs['pk'])
        return response

    @action(detail=True, methods=['get'])
    def report(self, request, pk=None):
        task = generate_event_report.delay(pk)
        result = task.get(timeout=10)
        if result:
            return Response(result)
        else:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def subscribe(self, request, pk=None):
        event = self.get_object()
        user = request.user
        event.participants.add(user)
        event.save()
        send_subscription_confirmation.delay(event.id, user.id)
        return Response({'status': 'subscribed'}, status=status.HTTP_200_OK)
