# -*- coding: utf-8 -*-

import pymysql.cursors
import requests
import os

# db.py: Connects and sends SQL queries to DB

auth_svc_url = os.getenv("AUTH_SVC_URL", "http://localhost:8000/")

def __get_connection(role):

    # and then run `python app.py`
    credentials = requests.get(auth_svc_url + role).json()

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