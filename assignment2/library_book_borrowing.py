member_dict = {}

available_books = {101, 102, 103, 104, 105, 106}

while True:

    member = input("Enter member name: ").lower()
    if member == "close":
        break

    book_id = int(input("Enter book id: "))
    borrow_request = (member, book_id)
    if book_id not in available_books:
        print("Unknown book id")
        continue
    
    if member not in member_dict:
        member_dict[member] = []
    if len(member_dict[member]) >= 3:
        print(f"{member} already has 3 books")
    else:
        member_dict[member].append(book_id)
        available_books.remove(book_id)
        print("Book Borrowed Successfully")

print("\nBorrowed Books")
for member, books in member_dict.items():
    print(member, ":", books)
print("\nAvailable Books:", available_books)