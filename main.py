class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                result += chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
            else:
                result += char
        return result

    def decrypt(self, text):
        return CaesarCipher(-self.shift).encrypt(text)


def main():
    while True:
        print("1. Shifrlash")
        print("2. Deshifrlash")
        print("3. Quit")
        choice = input("Tanlang: ")
        if choice == "1":
            text = input("Matn kiriting: ")
            shift = int(input("Shift kiriting: "))
            cipher = CaesarCipher(shift)
            encrypted_text = cipher.encrypt(text)
            print("Shifrlangan matn: ", encrypted_text)
        elif choice == "2":
            text = input("Shifrlangan matn kiriting: ")
            shift = int(input("Shift kiriting: "))
            cipher = CaesarCipher(shift)
            decrypted_text = cipher.decrypt(text)
            print("Deshifrlangan matn: ", decrypted_text)
        elif choice == "3":
            break
        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()