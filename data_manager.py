import database_common


@database_common.connection_handler
def get_comments(cursor):
    query = """
        SELECT id, name, text
        FROM comment
        ORDER BY id DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def create_comment(cursor, name, text):

    #query = f"INSERT INTO comment (name, text) VALUES ('{name}', '{text}')"
    query = """
           INSERT INTO COMMENT (name, text) 
           VALUES (name = %(username)s, text = %(text)s)
        """, {
        'username': name, 'text': text
    }
    cursor.execute(query)
