#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if letter in alpha:
            spot = (alpha.find(letter) + key) % 26  
            secret += alpha[spot]
        else:
            secret += letter  
    return secret

def decode(secret, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = ""

    for letter in secret:
        if letter in alpha:
            spot = (alpha.find(letter) - key) % 26 
            message += alpha[spot]
        else:
            message += letter  

    return message

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a shift key: "))

    encrypted = encode(message, key)
    print("Encrypted Message:", encrypted)

    decrypted = decode(encrypted, key)
    print("Decrypted Message:", decrypted)

if __name__ == "__main__":
    main()
