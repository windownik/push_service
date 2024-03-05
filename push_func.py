
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

cred = credentials.Certificate("cleaner-app.json")
firebase_admin.initialize_app(cred)


def send_push(main_msg_id: int, fcm_token: str, push_title: str, push_text: str, push_type: str,
              msg_json_body: str = "0", img_url: str = "0"):
    try:
        print("msg_id", main_msg_id)
        message = messaging.Message(
            data={'main_msg_id': f"{main_msg_id}",
                  'msg_json_body': msg_json_body,
                  'push_type': push_type,
                  },

            notification=messaging.Notification(
                title=push_title,
                body=push_text,
                image=None if img_url == '0' else img_url
            ),
            token=fcm_token
        )
        response = messaging.send(message)
    except Exception as _ex:
        print(_ex)


send_push(main_msg_id=1, push_type="msg", push_title="Test", push_text="example",
          fcm_token="cy-sB2w0RG6DCX67MWXtBt:APA91bGSpRNc61jZeNmYkeZMxl9s777nCje18fJEVpbbWc7yhxpeqFbvTPBRu9B5sITIoXReekOjo8xKcvRXN-Fn8M2--PW3Ajq3n5dWBLCVVfiaSSi5PIoJ_FDrozbXzHzfBMEZikzX")