books=[]
issued_books=[]
def add_book():
    name=input("Enter book name: ")
    books.append(name)
    print("Book added successfully")
def show_books():
    if len(books)==0:
        print("No books available")
    else:
        print("Books available:")
        for book in books:
            print(book)
def issue_book():
    if len(books)==0:
        print("No books available to issue")
    else:
        name=input("Enter book name to be issued:")
        if name in books:
            books.remove(name)
            issued_books.append(name)
            print("Book issued successfully")
        else:
            print("Book not available")
def return_book():
    name=input("Enter book name to be returned:")
    if name in issued_books:
        issued_books.remove(name)
        books.append(name)
        print("Book returned successfully")
    else:
        print("Book not found in issued books")
def library():
    while True:
        print("MENU")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        ch = int(input("Enter your choice: "))
        if ch==1:
            add_book()
        elif ch==2:
            show_books()
        elif ch==3:
            issue_book()
        elif ch==4:
            return_book()
        elif ch==5:
            print("Exited successfully")
            break
        else:
            print("Invalid choice. Please try again.")
library()