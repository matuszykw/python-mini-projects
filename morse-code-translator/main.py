from alphabet import encode, decode


def encode_text():
    text = input("Enter your text: ")
    morse_code = []
    for letter in text.upper():
        for i in encode:
            if letter == i:
                morse_code.append(encode[i])
    encoded_text = ' '.join(morse_code)
    print(encoded_text)
    

def decode_morse():
    code = input("Enter your morse code: ").upper()
    code_list = code.split(' ')
    text_letters = []
    for char in code_list:
        for i in decode:
            if char == i:
                text_letters.append(decode[i])
    decoded_text = ''.join(text_letters)
    print(decoded_text.lower())

choice = input("What do you want to do (encode/decode)? ")
if choice.lower() == 'encode':
    encode_text()
else:
    decode_morse()
