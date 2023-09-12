from database_util import get_mysql_connection


def get_user_login_data(connection, email: str):
    """
    This function takes as input a MySQL database connection object and an email address
    :param connection:
    :param email:
    :return: hashed password of the user
    """

    cursor = connection.cursor()
    query = ("SELECT password FROM users WHERE email = (%s)")

    cursor.execute(query, (email,))

    for (password) in cursor:
        return password


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


def insert_user(connection, bcrypt, user: dict):

    cursor = connection.cursor()
    query = ("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)")

    hashed_password = bcrypt.generate_password_hash(user['password']).decode('utf-8')
    data = (user['first_name'], user['last_name'], user['email'], hashed_password)
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
    # all_user_data = get_all_user_data(db_connection)
    # print(all_user_data)
    #
    # print("Entering new user data")
    #
    # new_user = {
    #     'first_name': 'dummy_f_name',
    #     'last_name': 'dummy_l_name',
    #     'email': 'dummy_f_name@gmail.com',
    #     'password': 'dummypassword'
    # }
    #
    # insert_user(db_connection, new_user)
    #
    # all_user_data = get_all_user_data(db_connection)
    # print(all_user_data)

    p = get_user_login_data(db_connection, 'jk@gmail.com')

    db_connection.close()
