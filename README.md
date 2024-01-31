# Caesar Cipher Encoder and Decoder

## Introduction
This Python program implements a Caesar Cipher encoder and decoder. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/RahmatillaMarvel/CeaserCipher.git
   cd CeaserCipher
   ```
2. Run the program:
   ```bash
   python ceasar_cipher.py
   ```
3. Enter the shift number, choose 'encode' or 'decode', and type your message.

## Code Examples

### Create an instance of the CeasarCipher class with the provided shift.
cipher = CeasarCipher(shift)

### Perform encryption or decryption based on the user's choice.
if direction == "encode":
    print(cipher.encrypt(text))
elif direction == "decode":
    print(cipher.decrypt(text))

## License
This project is licensed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for details.

## My portfolio site
You can find my portfolio at [rahmatilla.uz](https://rahmatilla.uz).

