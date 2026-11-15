def parse_member_id(member_id):
    member_type, number = member_id.split('-')
    return member_type.upper(), int(number)

def total_fine(days_csv):
    days = [int(d) for d in days_csv.split(',')]
    fine = 0
    for d in days:
        if d > 14:
            fine += (d - 14) * 2
    return fine

def shelf_code(title):
    words = title.split()
    return (words[0][0] + words[1][0]).upper()

def main():
    print("==== Running parse_member_id ====")
    user_input = input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    print("Shelf Code:", result)

if __name__ == "__main__":
    main()
