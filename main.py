class CeasarCipher:
    def __init__(self, shift_amount: int):
        """
        CeasarCipher class constructor.

        Parameters:
        - shift_amount (int): The shift amount for encryption and decryption.
        """
        self.shift_amount = shift_amount

    def encrypt(self, plain_text: str) -> str:
        """
        Encrypts the provided plain text using the Caesar Cipher.

        Parameters:
        - plain_text (str): The text to be encrypted.

        Returns:
        - str: The encrypted text.
        """
        cipher_text = ""

        if self.shift_amount > 26:
            self.shift_amount = self.shift_amount % 26

        for letter in plain_text:
            if letter == " " or not letter.isalnum():
                cipher_text += letter
                continue

            position = ord(letter)
            new_position = position + self.shift_amount

            if 97 > new_position > 57:
                new_position -= 10
            
            if new_position > 122:
                new_position -= 26
            
            new_letter = chr(new_position)
            cipher_text += new_letter

        return cipher_text

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the provided cipher text using the Caesar Cipher.

        Parameters:
        - cipher_text (str): The text to be decrypted.

        Returns:
        - str: The decrypted text.
        """
        plain_text: str = ""
        if self.shift_amount > 26:
            self.shift_amount = self.shift_amount % 26

        for letter in cipher_text:
            if letter == " " or not letter.isalnum():
                plain_text += letter
                continue

            position = ord(letter)
            new_position = position - self.shift_amount

            if 57 < new_position < 97:
                new_position += 26

            if new_position < 48:
                new_position += 10

            new_letter = chr(new_position)
            plain_text += new_letter

        return plain_text

if __name__ == "__main__":
    try:
        # Prompt the user to enter the shift number and convert it to an integer.
        shift: int = int(input("Type the shift number:\n"))
        
        # Create an instance of the CeasarCipher class with the provided shift.
        cipher = CeasarCipher(shift)

        # Prompt the user to choose 'encode' or 'decode' and convert to lowercase for case-insensitivity.
        direction: str = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

        # Check if the provided direction is valid; raise a ValueError if not.
        if direction not in ["encode", "decode"]:
            raise ValueError("Invalid input. Please type 'encode' or 'decode'.")

        # Prompt the user to enter the message to be encrypted or decrypted.
        text: str = input("Type your message:\n").lower()

        # Perform encryption or decryption based on the user's choice and print the result.
        if direction == "encode":
            print(cipher.encrypt(text))
        elif direction == "decode":
            print(cipher.decrypt(text))

    except ValueError as ve:
        # Handle ValueError exceptions, typically raised for invalid input.
        print(f"Error: {ve}")
