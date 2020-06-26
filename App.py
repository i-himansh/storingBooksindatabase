from utils import database
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice:  """

def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE).strip().lower()
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_books()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_books()
        elif user_input == 'd':
            prompt_delete_books()
        else:
            print("This is not a valid input, try again!")

        user_input = input(USER_CHOICE).strip().lower()


def prompt_add_books():
    name = input("Enter book name: ").strip().lower()
    author = input("Enter Author name: ").strip().lower()
    database.add_books(name,author)

def list_books():
    books = database.list_all_books()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']}, by {book['author']} , Read - {read}")

def prompt_read_books():
    name = input("Enter title of the book you have finshed: ").strip().lower()
    database.read_books(name)

def prompt_delete_books():
    name = input("Enter title of the book you want to remove: ").strip().lower()
    database.delete_books(name)



menu()

