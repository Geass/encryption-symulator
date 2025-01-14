from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

# Helper functions for encryption and decryption
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    encrypted = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift = ord(key[key_index % len(key)]) - 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            encrypted += char
    return encrypted

def vigenere_decrypt(text, key):
    decrypted = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift = -(ord(key[key_index % len(key)]) - 97)
            decrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            key_index += 1
        else:
            decrypted += char
    return decrypted

def base64_encrypt(text):
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text):
    try:
        return base64.b64decode(text).decode()
    except Exception:
        return "Invalid Base64 input"

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    text = data.get('text', '')
    algorithm = data.get('algorithm', '')
    key = data.get('key', '')
    
    if algorithm == 'caesar':
        shift = int(key) if key.isdigit() else 0
        result = caesar_encrypt(text, shift)
    elif algorithm == 'vigenere':
        result = vigenere_encrypt(text, key)
    elif algorithm == 'base64':
        result = base64_encrypt(text)
    else:
        result = "Unsupported algorithm"

    return jsonify({'result': result})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    text = data.get('text', '')
    algorithm = data.get('algorithm', '')
    key = data.get('key', '')

    if algorithm == 'caesar':
        shift = int(key) if key.isdigit() else 0
        result = caesar_decrypt(text, shift)
    elif algorithm == 'vigenere':
        result = vigenere_decrypt(text, key)
    elif algorithm == 'base64':
        result = base64_decrypt(text)
    else:
        result = "Unsupported algorithm"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
