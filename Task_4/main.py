# decorator for input check
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "This contact does not exist."
        except IndexError:
            return "Missing required input."
    return inner


@input_error
def parse_input(user_input):
    # Parses user input into command and arguments.
    parts = user_input.split()
    # if not parts: #empty command check
    #     return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts):
    # Adds a contact to the contacts dictionary.
    # if len(args) != 2:
    #     return "Invalid arguments. Please provide only name and phone."
    name, phone = args
    # if name in contacts:
    #     return f"The {name}'s contact already exists. Please use a different name."
    contacts[name] = phone
    return "Contact added."


@input_error
def find_contact(args, contacts):
    # Finds a contact's phone number by name.
    # if len(args) != 1:
    #     return "Invalid arguments. Please provide only name to find the phone number."
    name = args[0]
    return contacts.get(name, f"{name}'s number wasn't found.")


@input_error
def change_contact(args, contacts):
    # Changes a contact's phone number.
    # if len(args) != 2:
    #     return "Invalid arguments. Please provide name and phone."
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact changed."
    return f"{name} wasn't found."


@input_error
def show_all(contacts):
    # Displays all contacts from dic.
    # if not contacts:
    #     return "No contacts have been added yet."
    return "\n".join(f"Name: {name}, number: {number}" for name, number in contacts.items())


def main():
    # Main function.
    contacts = {}
    print("""
            _____             .___    .__              _____
  /     \   ____   __| _/_ __|  |   ____     /  |  |
 /  \ /  \ /  _ \ / __ |  |  \  | _/ __ \   /   |  |_
/    Y    (  <_> ) /_/ |  |  /  |_\  ___/  /    ^   /
\____|__  /\____/\____ |____/|____/\___  > \____   |
        \/            \/               \/       |__|
  ________ ________  .______________
 /  _____/ \_____  \ |   \__    ___/
/   \  ___  /   |   \|   | |    |
\    \_\  \/    |    \   | |    |
 \______  /\_______  /___| |____|
        \/         \/
    """)
    print("Welcome to the assistant bot!\n"
          "Please use the following commands:\n"
          "1. Hello\n"
          "2. Add\n"
          "3. Phone\n"
          "4. Get\n"
          "5. All\n"
          "6. Close or Exit\n")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "get":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
