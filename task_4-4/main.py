# the fuction takes the user input string and splits it into words using the split() method.
# it returns the first word as a cmd command and the rest as a list of *args arguments.
def parse_input(user_input: str):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()           # removes unnecessary spaces around the command and converts it to lowercase.
    return cmd, *args


# the function takes str arguments (name an phone) and the dictionary of the contact list
# it adds the name and the phone to the dictionary, creating a contact list for a user
def add_contact(args: str, contacts: dict) -> dict:
    try: 
        name, phone = args              # the argumnents are splitted into 2 variables
        if phone.isdigit():             # check if the phone number contains digits only
            name = name.strip().lower() # removes unnecessary spaces around the command and converts it to lowercase
            contacts[name] = phone      # if so, add the contact with the key as the name and value as a phone
            print("Contact added.")     # confirming the action by outputting the message for the user 
            return contacts
    except ValueError:                  # check for an ecxeption
        return "An error occured, please, try again."


# the function takes str arguments (name an phone) and the dictionary of the contact list
# it changes the phone number under the existing name and add it back to the dictionary, modifying a contact list for a user
def change_contact(args: str, contacts: dict) -> dict:
    try:
        name, phone = args                  # the argumnents are splitted into 2 variables
        name = name.strip().lower()         # removes unnecessary spaces around the command and converts it to lowercase
        if name in contacts:                # checking if the name is existing in the user contact list (dictionary with the names and phones)
            if phone.isdigit():             # check if the phone number contains digits only
                contacts[name] = phone      # if so, update the contact with the key as the name and value as a phone
                print("Contact updated.")   # confirming the action by outputting the message for the user 
                return contacts
        else:
            return "You don't have this contact in your list to change. Please, create the contact first."
    except ValueError:                      # check for an ecxeption
        return "An error occured, please, try again."


# the function takes the dictionary of the contact list
# it shows the entire contact list in the output for the user
def all_contacts(contacts: dict) -> str:
    contact_list = ""                               # the final return is going to be placed in this variable
    for key, value in contacts.items():             # issue the keys (names) and values (phone numbers) from the contact list (dict)
        contact_list += key + " - " + value + "\n"  # adding them to the str
    return contact_list


# the function takes str arguments (args == name) and the dictionary of the contact list
# it shows the phone number of the specific required name in the output for the user
def show_phone(args: str, contacts: dict) -> str:
    try:
        name = args[0].strip().lower()      # convert name to lowercase
        return contacts[name]               # issue the value (phone) under the key (name) we need
    except KeyError:                        # since args is a list, taking its zero element and checking for an exception
        return f"This contact doesn't exist in your contact list."
        
    
        
    

def main():

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
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
