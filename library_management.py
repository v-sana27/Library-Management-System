import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # apna mysql password
    database="library_db"
)

cursor = db.cursor()

print("✅ Connected to Library Database")


# -----------------------------------
# ADD BOOK
# -----------------------------------
def add_book():

    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    sql = """
    INSERT INTO books(book_name, author, status)
    VALUES(%s, %s, %s)
    """

    values = (book_name, author, "Available")

    cursor.execute(sql, values)

    db.commit()

    print("✅ Book Added Successfully")


# -----------------------------------
# VIEW BOOKS
# -----------------------------------
def view_books():

    cursor.execute("SELECT * FROM books")

    data = cursor.fetchall()

    print("\n====== BOOK RECORDS ======")

    for row in data:
        print(row)


# -----------------------------------
# ISSUE BOOK
# -----------------------------------
def issue_book():

    book_id = int(input("Enter Book ID to Issue: "))

    sql = "UPDATE books SET status=%s WHERE id=%s"

    values = ("Issued", book_id)

    cursor.execute(sql, values)

    db.commit()

    print("✅ Book Issued Successfully")


# -----------------------------------
# RETURN BOOK
# -----------------------------------
def return_book():

    book_id = int(input("Enter Book ID to Return: "))

    sql = "UPDATE books SET status=%s WHERE id=%s"

    values = ("Available", book_id)

    cursor.execute(sql, values)

    db.commit()

    print("✅ Book Returned Successfully")


# -----------------------------------
# DELETE BOOK
# -----------------------------------
def delete_book():

    book_id = int(input("Enter Book ID to Delete: "))

    sql = "DELETE FROM books WHERE id=%s"

    values = (book_id,)

    cursor.execute(sql, values)

    db.commit()

    print("✅ Book Deleted Successfully")


# -----------------------------------
# MAIN MENU
# -----------------------------------
while True:

    print("\n====== LIBRARY MANAGEMENT SYSTEM ======")

    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        print("✅ Program Closed")
        break

    else:
        print("❌ Invalid Choice")