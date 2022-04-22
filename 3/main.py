import psycopg2
import sys
import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many parameters!")
    sys.exit()
else:
    arg = sys.argv[1]


def check(email):
    """
    Check if user email is valid or not
    """
    if re.fullmatch(regex, email):
        pass
    else:
        print("Invalid Email")
        sys.exit(1)


def list_employee():
    """
    List all entries in employee table
    """
    conn = psycopg2.connect("dbname=testing user=postgres password=6927153a")
    cur = conn.cursor()
    try:
        cur.execute("SELECT first_name, last_name, email, code FROM EMPLOYEE")

        record = cur.fetchall()

        for row in record:
            print(("{:<15}" * len(row)).format(*row))
    finally:
        cur.close()
        conn.close()


def insert_employee():
    """
    Insert a new entry in employee table
    """

    conn = psycopg2.connect("dbname=testing user=postgres password=6927153a")
    cur = conn.cursor()

    try:
        fname = input("Enter the first name:")
        lname = input("Enter the last name:")
        new_email = input("Enter the email:")
        check(new_email)
        new_code = input("Enter the code:")

        if fname == "" and lname == "" and new_email == "" and new_code == "":
            print("Empty parameter(s)")
            sys.exit(1)

        cur.execute(f"SELECT * from EMPLOYEE WHERE code='{new_code}'")
        if cur.fetchall():
            print("Code is already taken!")
            sys.exit(1)

        cur.execute(
            "INSERT INTO EMPLOYEE(first_name, last_name, email,code) VALUES(%s, %s, %s, %s);",
            (
                fname,
                lname,
                new_email,
                new_code,
            ),
        )
        conn.commit()
        print("New entry inserted.")
    finally:
        cur.close()
        conn.close()


def update_employee():
    """
    Update an entry in employee table
    """
    conn = psycopg2.connect("dbname=testing user=postgres password=6927153a")
    cur = conn.cursor()

    try:
        code = input("Enter the existing code of the employee:")
        cur.execute(f"SELECT * from EMPLOYEE WHERE code='{code}'")
        if cur.fetchall():
            pass
        else:
            print("Code does not exist.")
            sys.exit(1)

        new_fname = input("Enter the new first name:")
        new_lname = input("Enter the new last name:")
        new_email = input("Enter the new email:")
        check(new_email)

        if new_fname == "" and new_lname == "" and new_email == "":
            print("Empty parameter(s)")
            sys.exit(1)

        cur.execute(
            """UPDATE EMPLOYEE SET first_name = %s, last_name = %s, email = %s WHERE code = %s;""",
            (new_fname, new_lname, new_email, code),
        )
        conn.commit()
        print("Entry updated.")
    finally:
        cur.close()
        conn.close()


def delete_employee():
    """
    Delete a record from the table
    """
    conn = psycopg2.connect("dbname=testing user=postgres password=6927153a")
    cur = conn.cursor()
    try:
        code = input("Enter the code of the employee to delete:")

        cur.execute(f"SELECT * from EMPLOYEE WHERE code='{code}'")
        if cur.fetchall():
            pass
        else:
            print("Code does not exist.")
            sys.exit(1)

        if code == "":
            print("Empty parameter")
            sys.exit(1)

        cur.execute("""DELETE FROM EMPLOYEE WHERE CODE = %(str)s;""", {"str": code})

        conn.commit()
        print("Entry deleted.")
    finally:
        cur.close()
        conn.close()


if arg == "list":
    list_employee()
elif arg == "add":
    insert_employee()
elif arg == "update":
    update_employee()
elif arg == "delete":
    delete_employee()
else:
    print("Incorrect parameter!")
