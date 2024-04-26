#atvaizduoti visus customerius
# atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis
# atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi
# atvaizduoti visus filmus ir kiek aktorių juose vaidino
# su pitono pagalba: nustatyti kuris nuomos punktas:
#--turi daugiau customerių
#--išnuomavo daugiau(ir kiek kiekvienas) filmų
#--kiek sugeneravo pajamų

print("1.atvaizduoti visus customerius")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")

    cursor = connection.cursor()
    query = "SELECT * FROM actor" # Replace with your desired query
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Surname: {row[2]}") # Access column data by index

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
print("Connection closed.")

print("2.atvaizduoti visus customerius ir stulpelį kuriame būtų atvaizduota kiek pinigų kiekvienas jų yra išleidęs nuomai, ir kiek filmų nuomavesis")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            cust.customer_id,
            cust.first_name,
            cust.last_name,
            SUM(pay.amount) AS isleistaSuma,
            COUNT(DISTINCT rent.rental_id) AS IsnuomotiFilmai
        FROM 
            customer cust
        JOIN 
            payment pay ON cust.customer_id = pay.customer_id
        JOIN 
            rental rent ON cust.customer_id = rent.customer_id
        GROUP BY 
            cust.customer_id, cust.first_name, cust.last_name
        ORDER BY 
            cust.customer_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        customer_id, first_name, last_name, isleistaSuma, IsnuomotiFilmai = row
        print(f"Customer ID: {customer_id}, Vardas: {first_name} {last_name}, IsleistaSuma: ${isleistaSuma}, Total Films Rented: {IsnuomotiFilmai}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")



print("3.atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            actor.actor_id,
            actor.first_name,
            actor.last_name,
            GROUP_CONCAT(film.title ORDER BY film.title SEPARATOR ', ') AS films_starred_in
        FROM 
            actor actor
        JOIN 
            film_actor filmactor ON actor.actor_id = filmactor.actor_id
        JOIN 
            film film ON filmactor.film_id = film.film_id
        GROUP BY 
            actor.actor_id, actor.first_name, actor.last_name
        ORDER BY 
            actor.actor_id
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        actor_id, first_name, last_name, films_starred_in = row
        print(f"Aktoriaus id: {actor_id}, Vardas: {first_name} {last_name}")
        print(f"Filmai kuriose vaidino: {films_starred_in}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")


print("4.atvaizduoti visus filmus ir kiek aktorių juose vaidino")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            film.film_id,
            film.title,
            COUNT(filmactor.actor_id) AS aktoriu_kiekis
        FROM 
            film film
        LEFT JOIN 
            film_actor filmactor ON film.film_id = filmactor.film_id
        GROUP BY 
            film.film_id, film.title
        ORDER BY 
            film.film_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        film_id, title, aktoriu_kiekis = row
        print(f"Filmo ID: {film_id}, Pavadinimas: {title}, Aktoriu kiekis: {aktoriu_kiekis}")

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

print("5.nustatyti kuris nuomos punktas: turi daugiau customerių")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query ="""
        SELECT 
            store.store_id,
            COUNT(cust.customer_id) AS nuomininkai
        FROM 
            store store
        JOIN 
            customer cust ON store.store_id = cust.store_id
        GROUP BY 
            store.store_id
        ORDER BY 
            nuomininkai DESC
    """
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        store_id, nuomininkai = result
        print(f"Store ID ir kiek turi klientu: {store_id}, Store ID ir kiek turi klientu: {nuomininkai}")
    else:
        print()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

print("6.nustatyti kuris nuomos punktas: išnuomavo daugiau(ir kiek kiekvienas) filmų")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
        SELECT 
            store.store_id,
            COUNT(invent.inventory_id) AS filmuSkaicius
        FROM 
            store store
        JOIN 
            inventory invent ON store.store_id = invent.store_id
        GROUP BY 
            store.store_id
        ORDER BY 
            filmuSkaicius DESC
    """

    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        store_id, filmuSkaicius = result
        print(f"Store ID ir kiek filmu isnuomota: {store_id}, Store ID ir kiek filmu isnuomota: {filmuSkaicius}")
    else:
        print()


except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")


print("7.nustatyti kuris nuomos punktas:kiek sugeneravo pajamų: ")

import mysql.connector

hostname = "localhost"
username = "root"
password = "Belenkas@23"
database = "sakila"

connection = None
cursor = None


try:
    connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
    print("Connection successful!")
    cursor = connection.cursor()
    query = """
            SELECT 
                store.store_id,
                SUM(payment.amount) AS pelnas
            FROM 
                store
            JOIN 
                staff ON store.manager_staff_id = staff.staff_id
            JOIN 
                payment ON staff.staff_id = payment.staff_id
            GROUP BY 
                store.store_id
            ORDER BY 
                pelnas DESC
            LIMIT 2
        """

    cursor.execute(query)
    results = cursor.fetchall()

    if results:
        for result in results:
            store_id, pelnas = result
            pelniukas = float(pelnas)
            print(f"Store ID: {store_id}, Pelnas: {pelniukas}")
    else:
        print()

except mysql.connector.Error as err:
    print(f"Connection error: {err}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
        print("Connection closed.")

