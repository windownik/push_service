import datetime, os

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


# Делаем запись новой строки в таблицу репортов
def write_report(cod_id: str, report_user_id: int, report_text: str):
    data = datetime.datetime.now()
    db = create_db_connect()
    with db.cursor() as cursor:
        cursor.execute(f"INSERT INTO reports (cod_id, report_user_id, report_text, data) "
                       f"VALUES ('{cod_id}', {report_user_id}, '{report_text}', '{data}') ON CONFLICT DO NOTHING;")
        db.commit()
        db.close()


# Делаем запись новой строки в базу данных
def update_user_data3(table: str,
                      data,
                      name: str,
                      data2,
                      name2: str,
                      data3,
                      name3: str,
                      data4,
                      name4: str,
                      id_data,
                      id_name: str = 'tg_id'):
    db = create_db_connect()
    with db.cursor() as cursor:
        cursor.execute(f"UPDATE {table} SET {name}=('{data}'),"
                       f"{name2}=('{data2}'),{name3}=('{data3}'), {name4}=('{data4}') "
                       f"WHERE {id_name}='{id_data}'")
        db.commit()

        db.close()


# Удаляем строку в таблице
def delete_line_in_table(data, table: str = 'all_categorys', name: str = 'id'):
    db = create_db_connect()
    with db.cursor() as cursor:
        cursor.execute(f"DELETE FROM {table} WHERE {name}='{data}'")
    db.commit()
    db.close()
