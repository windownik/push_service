import datetime
import json
import time

from push_func import send_push
from sql_func import create_db_connect, read_push, delete_msg_in_db


def start_push():
    db = create_db_connect()
    try:
        while True:
            if not db or db is None:
                db = create_db_connect()
            messages = read_push(db=db)
            for msg in messages:
                main_text = '0'
                img_url = '0'
                if msg[6] == 'img':
                    img_url = msg[5]
                else:
                    main_text = msg[4]
                    try:
                        main_text = json.loads(msg[4])
                    except:
                        pass
                send_push(fcm_token=msg[1], title=msg[2], short_text=msg[3], main_text=main_text, img_url=img_url,
                          push_type=msg[6], msg_id=msg[8])
                delete_msg_in_db(msg_id=msg[0], db=db)
            print(f'Send messages count :{len(messages)}')
            db.close()
            db = None
            time.sleep(5)

    except Exception as _ex:
        print('MAIN PROCESS ERROR -- ', _ex)
    finally:
        if db:
            db.close()


if __name__ == '__main__':
    print('Start work script')
    print(datetime.datetime.now())
    print('###############')
    start_push()
    print('###############')
    print('End work script')
    print(datetime.datetime.now())
