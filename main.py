# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QMessageBox
# import psycopg2
#
# class LibraryApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the user interface
#         self.isbn_label = QtWidgets.QLabel("ISBN")
#         self.isbn_input = QtWidgets.QLineEdit()
#         self.author_label = QtWidgets.QLabel("Author")
#         self.author_input = QtWidgets.QLineEdit()
#         self.date_label = QtWidgets.QLabel("Date")
#         self.date_input = QtWidgets.QLineEdit()
#         self.name_label = QtWidgets.QLabel("Name")
#         self.name_input = QtWidgets.QLineEdit()
#         self.add_book_button = QtWidgets.QPushButton("Add Book")
#         self.check_book_button = QtWidgets.QPushButton("Check Book")
#         self.take_book_button = QtWidgets.QPushButton("Take Book")
#
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.isbn_label)
#         layout.addWidget(self.isbn_input)
#         layout.addWidget(self.author_label)
#         layout.addWidget(self.author_input)
#         layout.addWidget(self.date_label)
#         layout.addWidget(self.date_input)
#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.add_book_button)
#         layout.addWidget(self.check_book_button)
#         layout.addWidget(self.take_book_button)
#         self.setLayout(layout)
#
#         # Connect signals to slots
#         self.add_book_button.clicked.connect(self.add_book)
#         self.check_book_button.clicked.connect(self.check_book)
#         self.take_book_button.clicked.connect(self.take_book)
#
#         # Set up the database connection
#         self.conn = psycopg2.connect(
#             host="localhost",
#             database="LIBRARY",
#             user="postgres",
#             password="witcher3"
#         )
#         self.cur = self.conn.cursor()
#
#     def add_book(self):
#         isbn = self.isbn_input.text()
#         author = self.author_input.text()
#         date = self.date_input.text()
#         name = self.name_input.text()
#
#         self.cur.execute("INSERT INTO books (isbn, author, date, name) VALUES (%s, %s, %s, %s)", (isbn, author, date, name))
#         self.conn.commit()
#
#         self.show_message("Book added successfully!")
#         self.clear_form()
#
#     def check_book(self):
#         isbn = self.isbn_input.text()
#         self.cur.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
#         book = self.cur.fetchone()
#         if book:
#             self.show_message("Book is available!")
#         else:
#             self.show_message("Book is not available!")
#
#     def take_book(self):
#         isbn = self.isbn_input.text()
#         self.cur.execute("DELETE FROM books WHERE isbn = %s", (isbn,))
#         self.conn.commit()
#
#         self.show_message("Book taken successfully!")
#         self.clear_form()
#
#     def clear_form(self):
#         self.isbn_input.setText("")
#         self.author_input.setText("")
#         self.date_input.setText("")
#         self.name_input.setText("")
#
#     def show_message(self, message):
#         msg = QMessageBox()
#         msg.setText(message)
#         msg.setWindowTitle("Notification")
#         msg.exec_()
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     window = LibraryApp()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QMessageBox
# import psycopg2
# import datetime
#
# class LibraryApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the user interface
#         self.isbn_label = QtWidgets.QLabel("ISBN")
#         self.isbn_input = QtWidgets.QLineEdit()
#         self.author_label = QtWidgets.QLabel("Author")
#         self.author_input = QtWidgets.QLineEdit()
#         self.date_label = QtWidgets.QLabel("Date")
#         self.date_input = QtWidgets.QLineEdit()
#         self.name_label = QtWidgets.QLabel("Name")
#         self.name_input = QtWidgets.QLineEdit()
#         self.pickup_label = QtWidgets.QLabel("Pick-Up Date")
#         self.pickup_input = QtWidgets.QLineEdit()
#         self.add_book_button = QtWidgets.QPushButton("Add Book")
#         self.check_book_button = QtWidgets.QPushButton("Check Book")
#         self.take_book_button = QtWidgets.QPushButton("Take Book")
#
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.isbn_label)
#         layout.addWidget(self.isbn_input)
#         layout.addWidget(self.author_label)
#         layout.addWidget(self.author_input)
#         layout.addWidget(self.date_label)
#         layout.addWidget(self.date_input)
#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.pickup_label)
#         layout.addWidget(self.pickup_input)
#         layout.addWidget(self.add_book_button)
#         layout.addWidget(self.check_book_button)
#         layout.addWidget(self.take_book_button)
#         self.setLayout(layout)
#
#         # Connect signals to slots
#         self.add_book_button.clicked.connect(self.add_book)
#         self.check_book_button.clicked.connect(self.check_book)
#         self.take_book_button.clicked.connect(self.take_book)
#
#         # Set up the database connection
#         self.conn = psycopg2.connect(
#             host="localhost",
#             database="LIBRARY",
#             user="postgres",
#             password="witcher3"
#         )
#         self.cur = self.conn.cursor()
#
#     def add_book(self):
#         isbn = self.isbn_input.text()
#         author = self.author_input.text()
#         date = self.date_input.text()
#         name = self.name_input.text()
#         pickup = self.pickup_input.text()
#
#         if not isbn.isdigit():
#             self.show_error_message("ISBN must be a number")
#             return
#         if len(isbn) != 13:
#             self.show_error_message("ISBN must be 13 characters long")
#             return
#         if not author:
#             self.show_error_message("Author name cannot be empty")
#             return
#         if not name:
#             self.show_error_message("Book name cannot be empty")
#             return
#         self.cur.execute("""
#                INSERT INTO books (isbn, author, date, name, pickup)
#                VALUES (%s, %s, %s, %s, %s)
#            """, (isbn, author, date, name, pickup))
#         self.conn.commit()
#         self.show_message("Book added successfully")
#
#     def check_book(self):
#         isbn = self.isbn_input.text()
#
#         if not isbn.isdigit():
#             self.show_error_message("ISBN must be a number")
#             return
#         if len(isbn) != 13:
#             self.show_error_message("ISBN must be 13 characters long")
#             return
#
#         self.cur.execute("""
#             SELECT * FROM books WHERE isbn=%s
#         """, (isbn,))
#         book = self.cur.fetchone()
#         if not book:
#             self.show_error_message("Book not found")
#             return
#
#         author, date, name, pickup = book[1:]
#         self.author_input.setText(author)
#         self.date_input.setText(date)
#         self.name_input.setText(name)
#         self.pickup_input.setText(pickup)
#         self.show_message("Book found")
#
#     def take_book(self):
#         isbn = self.isbn_input.text()
#
#         if not isbn.isdigit():
#             self.show_error_message("ISBN must be a number")
#             return
#         if len(isbn) != 13:
#             self.show_error_message("ISBN must be 13 characters long")
#             return
#
#         self.cur.execute("""
#             DELETE FROM books WHERE isbn=%s
#         """, (isbn,))
#         self.conn.commit()
#         self.show_message("Book taken")
#
#     def show_message(self, message):
#         QMessageBox.information(self, "Message", message)
#
#     def show_error_message(self, message):
#         QMessageBox.critical(self, "Error", message)
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     library_app = LibraryApp()
#     library_app.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QMessageBox
# import psycopg2
# import datetime
#
# class LibraryApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the user interface
#         self.isbn_label = QtWidgets.QLabel("ISBN")
#         self.isbn_input = QtWidgets.QLineEdit()
#         self.author_label = QtWidgets.QLabel("Author")
#         self.author_input = QtWidgets.QLineEdit()
#         self.date_label = QtWidgets.QLabel("Date")
#         self.date_input = QtWidgets.QLineEdit()
#         self.name_label = QtWidgets.QLabel("Name")
#         self.name_input = QtWidgets.QLineEdit()
#         self.pickup_label = QtWidgets.QLabel("Pick-Up Date")
#         self.pickup_input = QtWidgets.QLineEdit()
#         self.add_book_button = QtWidgets.QPushButton("Add Book")
#         self.check_book_button = QtWidgets.QPushButton("Check Book")
#         self.take_book_button = QtWidgets.QPushButton("Take Book")
#
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.isbn_label)
#         layout.addWidget(self.isbn_input)
#         layout.addWidget(self.author_label)
#         layout.addWidget(self.author_input)
#         layout.addWidget(self.date_label)
#         layout.addWidget(self.date_input)
#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.pickup_label)
#         layout.addWidget(self.pickup_input)
#         layout.addWidget(self.add_book_button)
#         layout.addWidget(self.check_book_button)
#         layout.addWidget(self.take_book_button)
#         self.setLayout(layout)
#
#         # Connect signals to slots
#         self.add_book_button.clicked.connect(self.add_book)
#         self.check_book_button.clicked.connect(self.check_book)
#         self.take_book_button.clicked.connect(self.take_book)
#
#         # Set up the database connection
#         self.conn = psycopg2.connect(
#             host="localhost",
#             database="LIBRARY",
#             user="postgres",
#             password="witcher3"
#         )
#         self.cur = self.conn.cursor()
#
#     def add_book(self):
#         isbn = self.isbn_input.text()
#         author = self.author_input.text()
#         date = self.date_input.text()
#         name = self.name_input.text()
#         pickup = self.pickup_input.text()
#
#         if not isbn.isdigit():
#             self.show_error_.dialog("ISBN must be a number.")
#             return
#
#
#         if len(author) == 0:
#             self.show_error_dialog("Author name cannot be empty.")
#             return
#
#         if len(name) == 0:
#             self.show_error_dialog("Book name cannot be empty.")
#             return
#
#         try:
#             pickup_date = datetime.datetime.strptime(pickup, '%Y-%m-%d')
#         except ValueError:
#             self.show_error_dialog("Invalid date format for pick-up. Use YYYY-MM-DD.")
#             return
#
#         self.cur.execute("INSERT INTO books (isbn, author, date, name, pickup) VALUES (%s, %s, %s, %s, %s)",
#                          (isbn, author, date, name, pickup))
#         self.conn.commit()
#         self.show_message_dialog("Book added successfully.")
#
#     def check_book(self):
#         isbn = self.isbn_input.text()
#         if not isbn.isdigit():
#             self.show_error_dialog("ISBN must be a number.")
#             return
#
#         self.cur.execute("SELECT * FROM books WHERE isbn=%s", (isbn,))
#         result = self.cur.fetchone()
#         if result is None:
#             self.show_error_dialog("Book not found.")
#         else:
#             self.isbn_input.setText(str(result[0]))
#             self.author_input.setText(result[1])
#             self.date_input.setText(result[2])
#             self.name_input.setText(result[3])
#             self.pickup_input.setText(str(result[4]))
#
#     def take_book(self):
#         isbn = self.isbn_input.text()
#         if not isbn.isdigit():
#             self.show_error_dialog("ISBN must be a number.")
#             return
#
#         self.cur.execute("DELETE FROM books WHERE isbn=%s", (isbn,))
#         self.conn.commit()
#         self.show_message_dialog("Book taken successfully.")
#
#     def show_error_dialog(self, message):
#         QMessageBox.critical(self, "Error", message)
#
#     def show_message_dialog(self, message):
#         QMessageBox.information(self, "Message", message)
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     library_app = LibraryApp()
#     library_app.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore
# from PyQt5.QtWidgets import QMessageBox
# import psycopg2
# import datetime
#
# class LibraryApp(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         # Set up the user interface
#         self.isbn_label = QtWidgets.QLabel("ISBN")
#         self.isbn_input = QtWidgets.QLineEdit()
#         self.author_label = QtWidgets.QLabel("Author")
#         self.author_input = QtWidgets.QLineEdit()
#         self.date_label = QtWidgets.QLabel("Date")
#         self.date_input = QtWidgets.QLineEdit()
#         self.name_label = QtWidgets.QLabel("Name")
#         self.name_input = QtWidgets.QLineEdit()
#         self.pickup_label = QtWidgets.QLabel("Pick-Up Date")
#         self.pickup_input = QtWidgets.QLineEdit()
#         self.add_book_button = QtWidgets.QPushButton("Add Book")
#         self.check_book_button = QtWidgets.QPushButton("Check Book")
#         self.take_book_button = QtWidgets.QPushButton("Take Book")
#
#         layout = QtWidgets.QVBoxLayout()
#         layout.addWidget(self.isbn_label)
#         layout.addWidget(self.isbn_input)
#         layout.addWidget(self.author_label)
#         layout.addWidget(self.author_input)
#         layout.addWidget(self.date_label)
#         layout.addWidget(self.date_input)
#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.pickup_label)
#         layout.addWidget(self.pickup_input)
#         layout.addWidget(self.add_book_button)
#         layout.addWidget(self.check_book_button)
#         layout.addWidget(self.take_book_button)
#         self.setLayout(layout)
#
#         # Connect signals to slots
#         self.add_book_button.clicked.connect(self.add_book)
#         self.check_book_button.clicked.connect(self.check_book)
#         self.take_book_button.clicked.connect(self.take_book)
#
#         # Set up the database connection
#         self.conn = psycopg2.connect(
#             host="localhost",
#             database="LIBRARY",
#             user="postgres",
#             password="witcher3"
#         )
#         self.cur = self.conn.cursor()
#
#     def add_book(self):
#         isbn = self.isbn_input.text()
#         author = self.author_input.text()
#         date = self.date_input.text()
#         name = self.name_input.text()
#         pickup = self.pickup_input.text()
#
#         if not isbn.strip() or not author.strip() or not date.strip() or not name.strip() or not pickup.strip():
#             self.show_message_box("Error", "All fields must be filled in.")
#             return
#         try:
#             self.cur.execute("INSERT INTO books (isbn, author, date, name, pickup) VALUES (%s, %s, %s, %s, %s)",
#                                  (isbn, author, date, name, pickup))
#             self.conn.commit()
#             self.show_message_box("Success", "Book added successfully.")
#         except Exception as e:
#             self.show_message_box("Error", str(e))
#
#     def check_book(self):
#         isbn = self.isbn_input.text()
#         if not isbn.strip():
#             self.show_message_box("Error", "ISBN field must be filled in.")
#             return
#
#         self.cur.execute("SELECT * FROM books WHERE isbn=%s", (isbn,))
#         result = self.cur.fetchone()
#
#         if result:
#             self.show_message_box("Book Details","Author: " + result[1] + "\nDate: " + str(result[2]) + "\nName: " + result[
#                                           3] + "\nPick-Up Date: " + str(result[4]))
#         else:
#             self.show_message_box("Error", "Book not found.")
#
#     def take_book(self):
#             isbn = self.isbn_input.text()
#
#             if not isbn.strip():
#                 self.show_message_box("Error", "ISBN field must be filled in.")
#                 return
#
#             self.cur.execute("UPDATE books SET pickup=%s WHERE isbn=%s", (datetime.datetime.now(), isbn))
#             self.conn.commit()
#             self.show_message_box("Success", "Book taken successfully.")
#
#     def show_message_box(self, title, message):
#         message_box = QMessageBox()
#         message_box.setWindowTitle(title)
#         message_box.setText(message)
#         message_box.exec_()
# app = QtWidgets.QApplication(sys.argv)
# library_app = LibraryApp()
# library_app.show()
# sys.exit(app.exec_())
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
import psycopg2
import datetime

class LibraryApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.isbn_label = QtWidgets.QLabel("ISBN")
        self.isbn_input = QtWidgets.QLineEdit()
        self.author_label = QtWidgets.QLabel("Author")
        self.author_input = QtWidgets.QLineEdit()
        self.publication_year_label = QtWidgets.QLabel("Publication Year")
        self.publication_year_input = QtWidgets.QLineEdit()
        self.title_label = QtWidgets.QLabel("Title")
        self.title_input = QtWidgets.QLineEdit()
        self.publisher_label = QtWidgets.QLabel("Publisher")
        self.publisher_input = QtWidgets.QLineEdit()
        self.edition_label = QtWidgets.QLabel("Edition")
        self.edition_input = QtWidgets.QLineEdit()
        self.language_label = QtWidgets.QLabel("Language")
        self.language_input = QtWidgets.QLineEdit()
        self.add_book_button = QtWidgets.QPushButton("Add Book")
        self.check_book_button = QtWidgets.QPushButton("Check Book")
        self.take_book_button = QtWidgets.QPushButton("Take Book")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.isbn_label)
        layout.addWidget(self.isbn_input)
        layout.addWidget(self.author_label)
        layout.addWidget(self.author_input)
        layout.addWidget(self.publication_year_label)
        layout.addWidget(self.publication_year_input)
        layout.addWidget(self.title_label)
        layout.addWidget(self.title_input)
        layout.addWidget(self.publisher_label)
        layout.addWidget(self.publisher_input)
        layout.addWidget(self.edition_label)
        layout.addWidget(self.edition_input)
        layout.addWidget(self.language_label)
        layout.addWidget(self.language_input)
        layout.addWidget(self.add_book_button)
        layout.addWidget(self.check_book_button)
        layout.addWidget(self.take_book_button)
        self.setLayout(layout)

        # Connect signals to slots
        self.add_book_button.clicked.connect(self.add_book)
        self.check_book_button.clicked.connect(self.check_book)
        self.take_book_button.clicked.connect(self.take_book)

        # Set up the database connection
        self.conn = psycopg2.connect(
            host="localhost",
            database="Library v2",
            user="postgres",
            password="witcher3"
        )
        self.cur = self.conn.cursor()

    def add_book(self):
        isbn = self.isbn_input.text()
        author = self.author_input.text()
        publication_year = self.publication_year_input.text()
        title = self.title_input.text()
        publisher = self.publisher_input.text()
        edition = self.edition_input.text()
        language = self.language_input.text()

        if not isbn.strip() or not author.strip() or not publication_year.strip() or not title.strip():
            self.show_message_box("Error", "ISBN, author, publication year, and title fields must be filled in.")
            return

        try:
            self.cur.execute("INSERT INTO books (isbn, author, publication_year, title, publisher, edition, language) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                 (isbn, author, publication_year, title, publisher, edition, language))
            self.conn.commit()
            self.show_message_box("Success", "Book added successfully.")
        except Exception as e:
            self.show_message_box("Error", str(e))

    def check_book(self):
        isbn = self.isbn_input.text()
        if not isbn.strip():
            self.show_message_box("Error", "ISBN field must be filled in.")
            return

        self.cur.execute("SELECT * FROM books WHERE isbn= %s", (isbn,))
        book = self.cur.fetchone()
        if book:
            availability = self.get_book_availability(isbn)
            if availability:
                self.show_message_box("Success", f"The book '{book[3]}' by {book[1]} is available.")
            else:
                self.show_message_box("Success", f"The book '{book[3]}' by {book[1]} is not available.")
        else:
            self.show_message_box("Error", "Book not found.")

    def take_book(self):
        isbn = self.isbn_input.text()
        if not isbn.strip():
            self.show_message_box("Error", "ISBN field must be filled in.")
            return

        availability = self.get_book_availability(isbn)

        if availability:
            self.cur.execute("INSERT INTO book_loans (isbn, date_loaned, date_due) VALUES (%s, %s, %s)",
                             (isbn, datetime.date.today(), datetime.date.today() + datetime.timedelta(days=14)))
            self.conn.commit()
            self.show_message_box("Success", f"The book with ISBN {isbn} has been loaned.")
        else:
            self.show_message_box("Error", f"The book with ISBN {isbn} is not available for loan.")

    def get_book_availability(self, isbn):
        self.cur.execute("SELECT * FROM book_loans WHERE isbn = %s AND date_returned IS NULL", (isbn,))
        book_loans = self.cur.fetchall()
        return len(book_loans) == 0

    def show_message_box(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    library_app = LibraryApp()
    library_app.show()
    sys.exit(app.exec_())