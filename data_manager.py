import database_common
from psycopg2 import sql


@database_common.connection_handler
def get_comments(cursor):
    query = """
        SELECT id, name, text
        FROM comment
        ORDER BY id DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def create_comment(cursor, name: str, text:str):

    #query = f"INSERT INTO comment (name, text) VALUES ('{name}', '{text}')"
    query = "INSERT INTO comment (name, text) VALUES (%s,%s)"
    cursor.execute(query,(name, text))
