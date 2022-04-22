import psycopg2
import sys

conn = psycopg2.connect("dbname=testing user=postgres password=6927153a")

cur = conn.cursor()


if len(sys.argv) == 1:
    print("Parameter cannot be empty!")
    sys.exit()
elif len(sys.argv) > 2:
    print("Too many parameters!")
    sys.exit()
else:
    arg = sys.argv[1]


def list_employee():

    cur.execute("SELECT * FROM EMPLOYEE")

    record = cur.fetchall()

    for row in record:
        print("Id = ", row[0])
        print("First name = ", row[1])
        print("Last name = ", row[2])
        print("Email = ", row[3])
        print("Unique code  = ", row[4], "\n")


def insert_employee():
    """
    Insert a new entry in employee table
    """

    fname = input("Enter the first name:")
    lname = input("Enter the last name:")
    new_email = input("Enter the email:")
    new_code = input("Enter the code:")

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

    cur.close()

    conn.close()

    print("New entry inserted.")


def update_employee():
    """
    Update a row in employee table
    """
    code = input("Enter the existing code of the employee:")
    new_fname = input("Enter the new first name:")
    new_lname = input("Enter the new last name:")
    new_email = input("Enter the new email:")

    if code != "":
        cur.execute(
            """UPDATE EMPLOYEE SET first_name = %s, last_name = %s, email = %s WHERE code = %s;""",
            (new_fname, new_lname, new_email, code),
        )
    else:
        print("Error: empty code!")

    conn.commit()

    cur.close()

    conn.close()

    print(cur.rowcount, "record affected")


def delete_employee():
    """
    Delete a record from the table
    """

    code = input("Enter the code of the employee to delete:")
    cur.execute("""DELETE FROM EMPLOYEE WHERE CODE = %(str)s;""", {"str": code})

    conn.commit()
    cur.close()
    conn.close()

    print(cur.rowcount, "records affected")


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
