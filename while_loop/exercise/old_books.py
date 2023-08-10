book = input()
counter = 0

while True:
    needed_book = input()

    if needed_book == book:
        print(f"You checked {counter} books and found it.")
        break

    if needed_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {counter} books.")
        break
    counter += 1
