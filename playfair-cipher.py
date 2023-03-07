def menu():
    eng_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    password = ""
    message = ""
    check_character = True

    while check_character:
        print("Enter the password")
        password = input()
        password = password.lower()
        password = password.replace("j", "i")
        password = password.replace(" ", "")

        for i in password:
            if i not in eng_alphabet:
                print("Wrong character detected.")
                check_character = True
                break
            else:
                check_character = False

    while True:
        print("1. Cipher message.")
        print("2. Decipher message.")
        option = input()
        if option == "1" or option == "2":
            option = int(option)
            break
        else:
            print("Wrong input.")

    while not check_character:
        print("Enter the message")
        message = input()
        message = message.lower()
        message = message.replace("j", "i")
        message = message.replace(" ", "")
        if len(message) % 2 == 1:
            message = message + "x"
        for i in message:
            if i not in eng_alphabet:
                print("Wrong character detected.")
                check_character = False
                break
            else:
                check_character = True
    return password, option, message


def index_of(letter, matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return i, index
        except:
            continue


def handle_new_alphabet(password):
    eng_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    x = 0
    new_alphabet = []

    # insert password into array and remove duplicates
    for i in password:
        eng_alphabet.insert(x, i)
        x += 1
    eng_alphabet = list(dict.fromkeys(eng_alphabet))

    # change array into 2d array
    for i in range(5):
        new_alphabet.append(eng_alphabet[i * 5:i * 5 + 5])

    return new_alphabet


def cipher_message(password, message):
    new_alphabet = handle_new_alphabet(password)
    final_message = ""

    for i in range(len(new_alphabet)):
        print(new_alphabet[i])
    print(message)

    message = list(message)
    for i in range(round(len(message) / 2)):
        y1, x1 = index_of(message[2 * i], new_alphabet)
        y2, x2 = index_of(message[(2 * i) + 1], new_alphabet)

        if y1 == y2 and x1 == x2:
            message[(2 * i) + 1] = "x"
            y2, x2 = index_of(message[(2 * i) + 1], new_alphabet)
            message[(2 * i)] = new_alphabet[y1][x2]
            message[(2 * i) + 1] = new_alphabet[y2][x1]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        elif y1 != y2 and x1 != x2:
            message[(2 * i)] = new_alphabet[y1][x2]
            message[(2 * i) + 1] = new_alphabet[y2][x1]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        elif y1 == y2 and x1 != x2:
            message[(2 * i)] = new_alphabet[y1][(x1 + 1) % 5]
            message[(2 * i) + 1] = new_alphabet[y2][(x2 + 1) % 5]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        elif y1 != y2 and x1 == x2:
            message[(2 * i)] = new_alphabet[(y1 + 1) % 5][x1]
            message[(2 * i) + 1] = new_alphabet[(y2 + 1) % 5][x2]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        else:
            final_message += message[(2 * i)] + message[(2 * i) + 1]

    return final_message


def decipher_message(password, message):
    new_alphabet = handle_new_alphabet(password)
    final_message = ""

    for i in range(len(new_alphabet)):
        print(new_alphabet[i])
    print(message)

    message = list(message)
    for i in range(round(len(message) / 2)):
        y1, x1 = index_of(message[2 * i], new_alphabet)
        y2, x2 = index_of(message[(2 * i) + 1], new_alphabet)

        if y1 != y2 and x1 != x2:
            message[(2 * i)] = new_alphabet[y1][x2]
            message[(2 * i) + 1] = new_alphabet[y2][x1]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        elif y1 == y2 and x1 != x2:
            message[(2 * i)] = new_alphabet[y1][(x1 - 1) % 5]
            message[(2 * i) + 1] = new_alphabet[y2][(x2 - 1) % 5]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        elif y1 != y2 and x1 == x2:
            message[(2 * i)] = new_alphabet[(y1 - 1) % 5][x1]
            message[(2 * i) + 1] = new_alphabet[(y2 - 1) % 5][x2]
            final_message += message[(2 * i)] + message[(2 * i) + 1]
        else:
            final_message += message[(2 * i)] + message[(2 * i) + 1]

    return final_message


if __name__ == '__main__':

    passwrd, opt, mess = menu()

    if opt == 1:
        print(cipher_message(passwrd, mess))
    else:
        print(decipher_message(passwrd, mess))

    exit(1)
