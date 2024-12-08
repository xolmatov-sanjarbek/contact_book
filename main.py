#ko'rish
#qo'shish
#olib tashlash

def add():
    contact_name = input("Ism: ")
    phone_number = input("Telefon raqam: ")
    contact_email = input("Email (ixtiyoriy): ")
    with open ("contacts.txt", 'a') as file:
        file.write(f"{contact_name} -- {phone_number} -- {contact_email}\n")


def view():
    with open('contacts.txt', 'r') as file:
        lines = file.readlines()
    for line in lines:
        print(line.strip())

def remove():
    remove_contact = input("Ism: ")
    with open("contacts.txt", 'r') as file:
        lines = file.readlines()
    with open("contacts.txt", 'w') as file:
        for line in lines:
            data = line.split()
            if data[0] != remove_contact:
                file.write(line)



while True:
    print("Kontaktlarni ko'rish (k), qo'shish (q), olib tashlash (o), chiqish uchun (exit)")
    ask = input('>>>')
    if ask == "exit":
        break
    elif ask == 'q':
        add()
    elif ask == 'k':
        view()
    elif ask == 'o':
        remove()