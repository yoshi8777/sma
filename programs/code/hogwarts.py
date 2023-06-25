def process_checkout_data(books, borrowers, checkouts):
    # Create a dictionary to store borrower names
    borrower_names = {}
    for borrower in borrowers:
        username, full_name = borrower.split('~')
        borrower_names[username] = full_name

    # Create a list to store checked out books
    checked_out_books = []
    for checkout in checkouts:
        username, accession_number, due_date = checkout.split('~')
        title = books[accession_number]
        full_name = borrower_names[username]
        checked_out_books.append((due_date, full_name, accession_number, title))

    # Sort the checked out books by due date and full name
    checked_out_books.sort(key=lambda x: (x[0], x[1]))

    # Print the details of checked out books
    for book in checked_out_books:
        print('~'.join(book))


def process_input_data(input_data):
    books = {}
    borrowers = []
    checkouts = []
    current_section = None

    for line in input_data:
        if line == 'Books':
            current_section = 'Books'
        elif line == 'Borrowers':
            current_section = 'Borrowers'
        elif line == 'Checkouts':
            current_section = 'Checkouts'
        elif line == 'EndOfInput':
            break
        else:
            if current_section == 'Books':
                accession_number, title = line.split('~')
                books[accession_number] = title
            elif current_section == 'Borrowers':
                borrowers.append(line)
            elif current_section == 'Checkouts':
                checkouts.append(line)

    process_checkout_data(books, borrowers, checkouts)


input_data = """Books
APM-001~Advanced Potion-Making
GWG-001~Gadding With Ghouls
APM-002~Advanced Potion-Making
DMT-001~Defensive Magical Theory
DMT-003~Defensive Magical Theory
GWG-002~Gadding With Ghouls
DMT-002~Defensive Magical Theory
Borrowers
SLY2301~Hannah Abbott
SLY2302~Euan Abercrombie
SLY2303~Stewart Ackerley
SLY2304~Bertram Aubrey
SLY2305~Avery
SLY2306~Malcolm Baddock
SLY2307~Marcus Belby
SLY2308~Katie Bell
SLY2309~Sirius Orion Black
Checkouts
SLY2304~DMT-002~2019-03-27
SLY2301~GWG-001~2019-03-27
SLY2308~APM-002~2019-03-14
SLY2303~DMT-001~2019-04-03
SLY2301~GWG-002~2019-04-03
EndOfInput"""

# Split the input data into lines and process it
input_lines = input_data.split('\n')
process_input_data(input_lines)

