import os

import psycopg2


password = os.environ.get("DATABASE_PASS")
host = os.environ.get("DATABASE_HOST")
port = os.environ.get("DATABASE_PORT")
db_name = os.environ.get("DATABASE_NAME")

password = 102015 if password is None else password
host = '127.0.0.1' if host is None else host
port = 5432 if port is None else port
db_name = 'cleaner_api' if db_name is None else db_name


def create_db_connect():
    data_base = psycopg2.connect(
        host=host,
        user='postgres',
        password=password,
        database=db_name,
        port=port
    )
    return data_base


def create_table_sending(db):
    """Создаем таблицу push_sending"""
    with db.cursor() as cursor:
        cursor.execute(
            f'''CREATE TABLE IF NOT EXISTS push_sending (
            push_id SERIAL PRIMARY KEY,
            user_id INTEGER DEFAULT 0,
            title TEXT DEFAULT '0',
            push_text TEXT DEFAULT '0',
            push_type TEXT DEFAULT '0',
            img_url TEXT DEFAULT '0',
            main_msg_id BIGINT DEFAULT 0,
            msg_json_body TEXT DEFAULT '0'
 )''')
        db.commit()


def read_push(db):
    """Читаем все пуш сообщения из базы данных"""
    with db.cursor() as cursor:
        cursor.execute(f"SELECT push_sending.push_id, push_sending.title, push_sending.push_text, "
                       f"push_sending.push_type, push_sending.img_url, push_sending.main_msg_id, "
                       f"push_sending.msg_json_body, all_users.push "
                       f"FROM push_sending JOIN all_users "
                       f"ON push_sending.user_id = all_users.user_id ORDER BY push_sending.push_id LIMIT 100;")
        data = cursor.fetchall()
        return data


def delete_msg_in_db(db, msg_id: int):
    """Удаляем пуш сообщение по id"""
    with db.cursor() as cursor:
        cursor.execute(f"DELETE FROM push_sending WHERE push_id=%s", (msg_id,))
    db.commit()
