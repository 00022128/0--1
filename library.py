import time

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' ({self.year})"


class Library:
    books = {}  # Dictionary to store books with author as key and list of (title, year) tuples as values
    borrowed = 0

    @staticmethod
    def add_book(title, author, year):
        book = (title, year)
        if author in Library.books:
            if book in Library.books[author]:
                print(f"Book '{title}' ({year}) by {author} already exists.")
                return
            Library.books[author].append(book)
        else:
            Library.books[author] = [book]
        print(f"New book '{title}' ({year}) by {author} has been added.")

    @staticmethod
    def remove_book(title, author, year):
        book = (title, year)
        if author in Library.books and book in Library.books[author]:
            Library.books[author].remove(book)
            if not Library.books[author]:  # Remove author key if no books left
                del Library.books[author]
            print(f"Book '{title}' ({year}) by {author} has been removed.")
        else:
            print(f"Book '{title}' ({year}) by {author} does not exist.")

    @staticmethod
    def to_borrow(title, author, year):
        book = (title, year)
        if author in Library.books and book in Library.books[author]:
            Library.borrowed += 1
            Library.books[author].remove(book)
            if not Library.books[author]:  # Remove author key if no books left
                del Library.books[author]
            print(f"Book '{title}' ({year}) by {author} has been borrowed.")
        else:
            print(f"Book '{title}' ({year}) by {author} does not exist.")

    @staticmethod
    def get_book(title, author, year):
        book = (title, year)
        if author in Library.books and book in Library.books[author]:
            print(f"Here is the book you searched for:\n'{title}' ({year}) by {author}")
        else:
            print("The book you're searching for was not found.")

def main():
    print("------ Welcome to Low IQ Library ------")
    while True:
        print("\n1. To add book")
        print("2. To remove book")
        print("3. To borrow book")
        print("4. To find book")
        print("5. Q to quit")
        choice = input("Enter your choice (1/2/3/4/Q): ").upper()

        if choice == "1":
            print("------ Entering Add Book system ------")
            new_title = input("Enter book title: ")
            new_author = input("Enter book author: ")
            new_year = input("Enter year of publication: ")
            Library.add_book(new_title, new_author, new_year)
        elif choice == "2":
            print("------ Entering Remove Book system ------")
            remove_title = input("Enter book title: ")
            remove_author = input("Enter book author: ")
            remove_year = input("Enter year of publication: ")
            Library.remove_book(remove_title, remove_author, remove_year)
        elif choice == "3":
            print("------ Entering Borrow Book system ------")
            borrow_title = input("Enter book title: ")
            borrow_author = input("Enter book author: ")
            borrow_year = input("Enter year of publication: ")
            Library.to_borrow(borrow_title, borrow_author, borrow_year)
        elif choice == "4":
            print("------ Entering Find Book system ------")
            find_title = input("Enter book title: ")
            find_author = input("Enter book author: ")
            find_year = input("Enter year of publication: ")
            Library.get_book(find_title, find_author, find_year)
        elif choice == "Q":
            print("Exiting.....")
            time.sleep(2)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
