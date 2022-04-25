import psycopg2
import sys

conn = psycopg2.connect("dbname=dvdrental user=postgres password=6927153a")
cur = conn.cursor()

# Table reference for testing:

#             employee_id              |              device_id               |   type
# --------------------------------------+--------------------------------------+-----------
# 70fb7a2a-7581-4312-9cdc-252c0ceedabf | 899854e0-0b7b-4698-8b53-958990b4f7b7 | CHECK_IN
# ff29fcd3-fdd8-43ff-bffe-8dd4a70ed102 | 4f173b7e-a24f-4781-8e09-3db4bcdee642 | CHECK_IN
# d80b7cc9-99d8-40f6-a087-13a33ba7bbd7 | 791fcd16-66df-44f7-b510-561abf0904a5 | CHECK_OUT
# d80b7cc9-99d8-40f6-a087-13a33ba7bbd7 | 791fcd16-66df-44f7-b510-561abf0904a5 | CHECK_OUT
# 0c6e88ae-8a3f-478b-9a05-b149d9123d23 | 0c31a77e-e59a-4e29-805f-91c7369a679c | CHECK_IN

if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many parameters!")
    sys.exit()
else:
    arg = sys.argv[1]


def check_in(conn, cur):
    """
    Updates an entry usage type to "CHECK_IN"
    """
    try:
        employee_id = input("Enter employee id:")
        device_id = input("Enter device id:")

        if employee_id == "" or device_id == "":
            print("Empty parameter(s)")
            sys.exit(1)

        cur.execute(
            f"SELECT type from USAGE WHERE type = 'CHECK_IN' and device_id = '{device_id}'"
        )
        if cur.fetchall():
            print("Device already checked in.")
            sys.exit(1)
        else:
            pass

        cur.execute(
            f"UPDATE USAGE SET type = 'CHECK_IN' WHERE usage.employee_id = '{employee_id}' AND usage.device_id = '{device_id}'"
        )
        conn.commit()
        print("Entry updated.")
    finally:
        conn.close()
        cur.close()


def check_out(conn, cur):
    """
    Updates an entry usage type to "CHECK_OUT"
    """
    try:
        employee_id = input("Enter id:")
        device_id = input("Enter device id:")

        if employee_id == "" or device_id == "":
            print("Empty parameter(s)")
            sys.exit(1)

        cur.execute(
            f"SELECT type from USAGE WHERE type = 'CHECK_OUT' and device_id = '{device_id}'"
        )
        if cur.fetchall():
            print("Device already checked out.")
            sys.exit(1)
        else:
            pass

        cur.execute(
            f"UPDATE USAGE SET type = 'CHECK_IN' WHERE usage.employee_id = '{employee_id}' AND usage.device_id = '{device_id}'"
        )
        conn.commit()
        print("Entry updated.")
    finally:
        conn.close()
        cur.close()


if arg == "check_in":
    check_in(conn, cur)
elif arg == "check_out":
    check_out(conn, cur)
else:
    print("Incorrect parameter!")
