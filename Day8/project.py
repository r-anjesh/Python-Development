from logo import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = 'yes'
while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(plain_text,shift_amount,direction):
            
        def encrypt(plain_text,shift_amount):
            cipher_text = ''
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position + (shift_amount%26)
                    if new_position > 25:
                        cipher_text += alphabet[new_position-26]
                    else:
                        cipher_text += alphabet[new_position]
                else:
                    cipher_text += letter
            print(f'The encodded code is {cipher_text}')


        def decrypt(plain_text,shift_amount):
            caesar_text = ''
            for letter in plain_text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position - (shift_amount%26)
                    if new_position < 0:
                        caesar_text += alphabet[26+new_position]
                    else:
                        caesar_text += alphabet[new_position]
                else:
                    caesar_text += letter
            print(f"The decoded code is {caesar_text}")

        if direction == 'encode':
            encrypt(text,shift)
        elif direction == 'decode':
            decrypt(text,shift)


    caesar(text,shift,direction)
    restart = input("Do You want to restart : type 'Yes' or 'No : ").lower()
    if restart == 'no':
        print("Have a nice day 😘\nGoodBye")
