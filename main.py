import datetime
import time

from push_func import send_push
from sql_func import create_db_connect, read_push, delete_msg_in_db, create_table_sending


def start_push():
    db = create_db_connect()
    create_table_sending(db)
    try:
        while True:
            if not db or db is None:
                db = create_db_connect()
            messages = read_push(db=db)
            for msg in messages:
                send_push(fcm_token=msg[7], push_title=msg[1], push_text=msg[2], push_type=msg[3], img_url=msg[4],
                          main_msg_id=msg[5], msg_json_body=msg[6])
                delete_msg_in_db(msg_id=msg[0], db=db)
            print(f'Send messages count :{len(messages)}')
            db.close()
            db = None
            time.sleep(4)

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
