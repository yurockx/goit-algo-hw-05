from functools import wraps


def input_error(func):
    # Decorator
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__.lower() == "add_contact":
                return "Please enter name and phone to add a new contact."
            if func.__name__.lower() == "change_contact":
                return "Please enter correct name and a new phone to change the contact. Type 'all' to see contacts present"
            else:
                return None, "Please enter name and phone.1"
        # 'KeyError is not used but bypassed in line 50 by .get() plus default value, but left for future'
        except KeyError:
            return None, "This contact does not exist."
        except IndexError:
            if func.__name__.lower() == "find_contact":
                return "No Name was provided. Please enter the name or type 'all' to see all"
            else:
                return None, "Missing required input."
    return inner


@input_error
def parse_input(user_input):
    # 'Parses user input into command and arguments.'
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:3]
    return cmd, args


@input_error
def add_contact(args, contacts):
    # 'Adds a contact to the contacts dictionary.'
    name, phone = args
    if name in contacts:
        return f"The {name}'s contact already exists. Please use a different name."
    contacts[name] = phone
    return "Contact added."


@input_error
def find_contact(args, contacts):
    # 'Finds a contact's phone number by name.'
    name = args[0]
    return contacts.get(name, f"{name}'s number wasn't found.")


@input_error
def change_contact(args, contacts):
    # 'Changes a contact's phone number.'
    name, new_number = args
    if name in contacts:
        contacts[name] = new_number
        return "Contact changed."
    return f"{name} wasn't found."


@input_error
def show_all(contacts):
    # 'Displays all contacts from dic.'
    return "\n".join(f"Name: {name}, number: {number}" for name, number in contacts.items())


def main():
    # 'Main loop.'
    contacts = {}
    print("""
  __  __           _       _        _____ 
 |  \/  |         | |     | |      | ____|
 | \  / | ___   __| |_   _| | ___  | |__  
 | |\/| |/ _ \ / _` | | | | |/ _ \ |___ \ 
 | |  | | (_) | (_| | |_| | |  __/  ___) |
 |_|  |_|\___/ \__,_|\__,_|_|\___| |____/                                                                          
  ________ ________  .______________                 
 /  _____/ \_____  \ |   \__    ___/                 
/   \  ___  /   |   \|   | |    |                    
\    \_\  \/    |    \   | |    |                    
 \______  /\_______  /___| |____|                    
        \/         \/""")
    print("Welcome to the assistant bot!\n"
          "Available commands:\n"
          "hello                  - Greet the bot\n"
          "add <name> <phone>     - Add new contact\n"
          "phone <name>           - Show contact number\n"
          "change <name> <number> - Change contact number\n"
          "all                    - Show all contacts\n"
          "help                   - Show this help\n"
          "close / exit           - Quit the program\n")
    
    # 'Bot commands'
    commands = {
        "add": add_contact,
        "phone": find_contact,
        "change": change_contact,
        "all": lambda args, contacts: show_all(contacts),
    }

    while True:
        user_input = input("Enter a command: ")
        command_result = parse_input(user_input)
        # to get clean error message for no command input
        if command_result[0] is None:
            print(command_result[1])
            continue

        command, args = command_result

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print("Available commands: hello, add, phone, change, all, help, close, exit")
        elif command in commands:
            result = commands[command](args, contacts)
            print(result)
        else:
            print("Invalid command. Type 'help' to see available options.")


if __name__ == "__main__":
    main()
