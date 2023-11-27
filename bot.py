import re


def validate_phone(phone):
    if re.match(r"^\+?\d{10,}$", phone):
        return True
    else:
        return False


def add_contact(contacts, name, phone):
    if validate_phone(phone):
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid phone number. Please enter a valid phone number."


def change_contact(contacts, name, new_phone):
    if not validate_phone(new_phone):
        return "Invalid phone number. Please enter a valid phone number."
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(contacts, name):
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# Show available commands.
def show_info():
    info_message = (
        "Available commands:\n"
        "add [name] [phone] - Add a new contact with a valid phone number.\n"
        "change [name] [new phone] - Change an existing contact's phone number.\n"
        "phone [name] - Display a contact's phone number.\n"
        "all - Show all saved contacts and their phone numbers.\n"
        "exit or close - Close the program.\n"
        "hello - Greeting from the assistant.\n"
        "info - Show available commands."
    )
    return info_message


# Interprets user commands.
def main():
    contacts = {}
    while True:
        command = input("Enter a command: ").strip().lower()

        # Skip empty commands.
        if len(command) == 0:
            continue

        # Initial commands.
        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "info":
            print(show_info())
        else:
            parts = command.split()
            cmd, args = parts[0], parts[1:]

            # Functional commands.
            if cmd == "add" and len(args) == 2:
                print(add_contact(contacts, *args))
            elif cmd == "change" and len(args) == 2:
                print(change_contact(contacts, *args))
            elif cmd == "phone" and len(args) == 1:
                print(show_phone(contacts, *args))
            elif cmd == "all" and len(args) == 0:
                print(show_all(contacts))
            else:
                print("Invalid command.")


if __name__ == "__main__":
    main()
