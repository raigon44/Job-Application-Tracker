from database_util import get_mysql_connection


def get_all_user_data(connection):

    cursor = connection.cursor()
    query = ("SELECT first_name, last_name FROM users")

    cursor.execute(query)
    response = []
    for (first_name, last_name) in cursor:
        response.append(
            {
                'first_name': first_name,
                'last_name': last_name
            }
        )

    return response


def insert_user(connection, user: dict):

    cursor = connection.cursor()
    query = ("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)")

    data = (user['first_name'], user['last_name'], user['email'], user['password'])
    cursor.execute(query, data)

    connection.commit()

    return


def delete_user(connection, user_id: int):

    cursor = connection.cursor()
    query = ("DELETE FROM users WHERE user_id="+str(user_id))

    cursor.execute(query)

    connection.commit()

    return


if __name__ == '__main__':
    db_connection = get_mysql_connection()
    all_user_data = get_all_user_data(db_connection)
    print(all_user_data)

    print("Entering new user data")

    new_user = {
        'first_name': 'dummy_f_name',
        'last_name': 'dummy_l_name',
        'email': 'dummy_f_name@gmail.com',
        'password': 'dummypassword'
    }

    insert_user(db_connection, new_user)

    all_user_data = get_all_user_data(db_connection)
    print(all_user_data)

    db_connection.close()
