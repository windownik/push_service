
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

cred = credentials.Certificate("cleaner-app.json")
firebase_admin.initialize_app(cred)


def send_push(fcm_token: str, title: str, short_text: str, push_type: str, description: str):
    try:
        message = messaging.Message(
            data={'title': title,
                  'short_text': short_text,
                  'description': description,
                  'push_type': push_type,
                  },
            notification=messaging.Notification(
                title=title,
                body=short_text,
            ),
            token=fcm_token
        )
        response = messaging.send(message)
    except Exception as _ex:
        print(_ex)
