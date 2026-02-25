def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\nYour Notes:")
            print(file.read())
    except FileNotFoundError:
        print("No notes found.")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        break
    else:
        print("Invalid option")
def delete_notes():
    open("notes.txt", "w").close()
    print("All notes deleted!")
Add menu option inside loop:
print("4. Delete All Notes")
And inside conditions:
elif choice == "4":
    delete_notes()
