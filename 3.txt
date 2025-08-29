def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def change_value_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and NEW phone please."

    return inner

def key_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact is not found."
        
    return inner

def index_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter a name of contact"
        
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@index_error
@input_error
def add_contact(args, contacts): # функція для додавання нового контакту
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' added."

@index_error
@change_value_error
@key_error
def change_contact(args, contacts): # функція для заміни імені  контакту
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for '{name}' updated."
    else:
        raise KeyError(name)

@index_error
@key_error
def get_phone(args, contacts):  # функція для відображення контакту за запитом
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError(name)
    

def show_all(contacts):  # функція для відображення всіх збережених контактів
    if not contacts:
        return "No contacts saved."
    result = ["Contacts list:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():  # основна функція для інтерактивного спілкування з користувачем
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()