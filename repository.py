import psycopg2


def get_connection():
    connection = psycopg2.connect("dbname=demo "
                                  "host=localhost "
                                  "port=5432 "
                                  "user=postgres "
                                  "password=root ")

    cursor = connection.cursor()

    return connection, cursor


def create_new_partner(partner_type,
                 name,
                 director_first_name,
                 director_second_name,
                 director_sur_name,
                 email,
                 phone,
                 address,
                 rating=0
                 ):

    connection, cursor = get_connection()

    if not rating:
        rating = 0

    try:
        cursor.execute("select MAX(partner_id) FROM partners")
        index = cursor.fetchone()[0]
        cursor.execute('INSERT INTO partners(partner_id, partner_type, '
                       'partner_name, '
                       'director_first_name, '
                       'director_last_name, director_sur_name,'
                       'email, phone, address_index, address_district, '
                       'address_town, '
                       'address_street, address_house, inn, rating) '
                       'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       [index+1, partner_type, name, director_first_name,
                        director_second_name, director_sur_name,
                        email, phone, address.split(', ')[0],
                        address.split(', ')[1], address.split(', ')[2],
                        address.split(', ')[3], address.split(', ')[4],
                        '0', rating
                        ])
        connection.commit()

        index += 1
        cursor.close()
        connection.close()
    except:
        raise Exception()


def update_partner(id, partner_type,
                       name,
                       director_first_name,
                       director_second_name,
                       director_sur_name,
                       email,
                       phone,
                       address,
                       rating=0
                       ):
    connection, cursor = get_connection()

    if not rating:
        rating = 0

    cursor.execute('UPDATE partners '
                   'SET '
                   'partner_type = %s, '
                   'partner_name = %s, '
                   'director_first_name = %s, '
                   'director_last_name = %s, director_sur_name = %s, '
                   'email = %s, phone = %s, address_index = %s, address_district = %s, '
                   'address_town = %s, '
                   'address_street = %s, address_house = %s, inn = %s, rating = %s '
                   'WHERE partner_id = %s',
                   [partner_type, name, director_first_name,
                    director_second_name, director_sur_name,
                    email, phone, address.split(', ')[0],
                    address.split(', ')[1], address.split(', ')[2],
                    address.split(', ')[3], address.split(', ')[4],
                    '0', rating, id
                    ])
    connection.commit()

    cursor.close()
    connection.close()