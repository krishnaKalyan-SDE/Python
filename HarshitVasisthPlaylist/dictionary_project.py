contact_book={}
def add_contact(name,phone_no):
    contact_book[name]=phone_no
    if len(phone_no)!=10:
            print("Enter valid phone number")
    else:
         print(f"conact {name} added with phone number {phone_no}")
   

def view_contact():
    if not contact_book:
        print("No contact available")
    for name,phone_no in contact_book.items():
        print(f"Name: {name}, Phone Number: {phone_no}")

def update_contact(name,new_phone_no):
    if name in contact_book:
      contact_book[name]=new_phone_no
    else:
      print("contact not found")
    if len(new_phone_no)!=10:
            print("Enter valid phone no")
    else:
            print(f"Contact {name} updated to phone number {new_phone_no}.")

def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"contact {name} deleted successfully")
    else:
        print("conatct not found")

def search_contact(name):
    data=contact_book.get(name)
    if data:
         print(f"Contact found: Name: {name}, Phone Number: {data}")
    else:
        print("conatct not found")

while True:
    print("\nContact Book Menu: ")
    print("1. Add Contact")
    print("2. view Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")


    choice=input("Enter choice: ")

    if choice=='1':
        name=input("Enter contact name: ")
        phone_no=input("Enter phone number: ")
        add_contact(name,phone_no)
    elif choice=='2':
        view_contact()
    elif choice=='3':
        name=input("Enter contact name to update: ")
        new_phone_no=input("Enter new phone number: ")
        update_contact(name,new_phone_no)
    elif choice=='4':
        name=input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice=='5':
        name=input("Enter contact name to search: ")
        search_contact(name)
    elif choice=='6':
        print(f"Thankyou{"\U0001F64F"} for using our service.")
        break
    else:
        print("Invalid choice.Please enter a number between 1 and 6.")






   
