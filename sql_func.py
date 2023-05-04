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


# Собираем все записи с фильтрацией по 1 параметру
def read_push(db):
    with db.cursor() as cursor:
        cursor.execute(f"SELECT sending.id, all_users.push, sending.title, sending.short_text, sending.main_text, "
                       f"sending.img_url, sending.push_type, all_users.user_id FROM sending JOIN all_users "
                       f"ON sending.user_id = all_users.user_id ORDER BY id LIMIT 100;")
        data = cursor.fetchall()
        return data


# Удаляем строку в таблице
def delete_msg_in_db(db, msg_id: int):
    with db.cursor() as cursor:
        cursor.execute(f"DELETE FROM sending WHERE id=%s", (msg_id,))
    db.commit()
