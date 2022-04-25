import psycopg2
import sys

conn = psycopg2.connect("dbname=dvdrental user=postgres password=6927153a")
cur = conn.cursor()

if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many parameters!")
    sys.exit()
else:
    arg = sys.argv[1]


def list_all(conn, cur):
    """
    Lists all entries
    """

    try:
        code = input("Enter:")
        cur.execute(
            f"SELECT usage.date, usage.Type, DEVICE.description, DEVICE.brand, DEVICE.type, DEVICE.code FROM USAGE JOIN DEVICE ON device_id = DEVICE.id JOIN EMPLOYEE ON EMPLOYEE.id = employee_id WHERE EMPLOYEE.code = '{code}'"
        )
        record = cur.fetchall()

        for row in record:
            print(("{} " * len(row)).format(*row))
    finally:
        conn.close()
        cur.close()


def list_in(conn, cur):
    """
    Lists checked in entries
    """
    try:
        code = input("Enter:")
        cur.execute(
            f"SELECT usage.date, DEVICE.description, DEVICE.brand, DEVICE.type, DEVICE.code FROM USAGE LEFT JOIN DEVICE ON device_id = DEVICE.id JOIN EMPLOYEE ON EMPLOYEE.id = employee_id WHERE usage.Type = 'CHECK_IN' AND EMPLOYEE.code = '{code}'"
        )
        record = cur.fetchall()

        for row in record:
            print(("{} " * len(row)).format(*row))
    finally:
        conn.close()
        cur.close()


def list_out(conn, cur):
    """
    Lists all checked out entries
    """
    try:
        code = input("Enter:")
        cur.execute(
            f"SELECT usage.date, DEVICE.description, DEVICE.brand, DEVICE.type, DEVICE.code FROM USAGE LEFT JOIN DEVICE ON device_id = DEVICE.id JOIN EMPLOYEE ON EMPLOYEE.id = employee_id WHERE usage.Type = 'CHECK_OUT' AND EMPLOYEE.code = '{code}'"
        )
        record = cur.fetchall()

        for row in record:
            print(("{} " * len(row)).format(*row))
    finally:
        conn.close()
        cur.close()


if arg == "list_all":
    list_all(conn, cur)
elif arg == "list_in":
    list_in(conn, cur)
elif arg == "list_out":
    list_out(conn, cur)
else:
    print("Incorrect parameter!")
