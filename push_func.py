
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

cred = credentials.Certificate("cleaner-app.json")
firebase_admin.initialize_app(cred)


def send_push(fcm_token: str, title: str, short_text: str, push_type: str, main_text: str, img_url: str):
    try:
        print(img_url)
        message = messaging.Message(
            data={'title': title,
                  'short_text': short_text,
                  'main_text': main_text,
                  'img_url': img_url,
                  'push_type': push_type,
                  },

            notification=messaging.Notification(
                title=title,
                body=short_text,
                image=None if img_url == '0' else img_url
            ),
            token=fcm_token
        )
        response = messaging.send(message)
    except Exception as _ex:
        print(_ex)
