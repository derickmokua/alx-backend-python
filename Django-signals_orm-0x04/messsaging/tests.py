from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class SignalTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='alice', password='alicepwd')
        self.receiver = User.objects.create_user(username='bob', password='bobpwd')

    def test_notification_created_on_new_message(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, content="Hello Bob")
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.user, self.receiver)
        self.assertEqual(notification.message, msg)
