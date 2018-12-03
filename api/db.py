import pymysql.cursors
import requests

# db.py: Connects and sends SQL queries to DB


def __get_connection(role):
    # Don't hardcode
    auth_svc_address = "http://auth_svc"
    auth_svc_port = "8080"
    auth_svc_endpoint = "/"

    # For local testing run make start - stop this container only
    # Uncomment the following details and comment the above:

    # auth_svc_address = "http://localhost"
    # auth_svc_port = "8000"
    # auth_svc_endpoint = "/"

    # and then run `python app.py`
    credentials = requests.get(
        auth_svc_address + ":" + auth_svc_port + auth_svc_endpoint + role).json()

    return pymysql.connect(
        host=credentials["host"],
        db=credentials["db"],
        charset=credentials["charset"],
        user=credentials["user"],
        password=credentials["password"],
        cursorclass=pymysql.cursors.DictCursor)


def queryDB(querySQL, role="default"):
    connection = __get_connection(role)
    try:
        resultsArray = []
        with connection.cursor() as cursor:
            cursor.execute(querySQL)
            resultset = cursor.fetchall()

            for result_item in resultset:
                resultsArray.append(result_item)

    except pymysql.err.ProgrammingError as except_detail:
        connection.close()
        return("pymysql.err.ProgrammingError: «{}»".format(except_detail))
    finally:
        connection.close()
        return resultsArray


def mutateDB(querySQL, role="default"):
    connection = __get_connection(role)
    try:
        with connection.cursor() as cursor:
            cursor.execute(querySQL)
            connection.commit()
        connection.close()
        return "Done"
    except pymysql.err.ProgrammingError as except_detail:
        connection.close()
        return("pymysql.err.ProgrammingError: «{}»".format(except_detail))
