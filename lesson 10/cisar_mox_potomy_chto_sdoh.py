alphabet = bykvi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

while not should_end: # пока should_end != True

    text = input("Введи сообщение: ")
    text = list(text)
    shift = int(input("Сдвиг: "))


    cipher_text = ""
    for letter in text:
        if letter == "":
            cipher_text += letter
        else:
            position = alphabet.index(letter) # какой индекс у леттер
            if position + shift > len(alphabet): # вышли за верх
                new_position = position + shift - len(alphabet)
            elif position + shift < 0:  # вышли за низ
                new_position = position + shift + len(alphabet)
            else:
                new_position = position + shift
            cipher_text += alphabet[new_position]