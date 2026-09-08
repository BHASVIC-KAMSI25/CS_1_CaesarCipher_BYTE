# B.Y.T.E Task 1: Caesar Cipher

A Python Flask web application that implements the Caesar Cipher for text encryption and decryption.

## Features

* Encrypts plaintext using a configurable shift value.
* Decrypts ciphertext back to the original text.
* Supports positive and negative shift values.
* Preserves spaces, numbers and punctuation.
* Supports both uppercase and lowercase letters.
* Provides a simple web-based interface.
* Can be deployed as a publicly accessible web application.

## How the Caesar Cipher Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

For example, with a shift of 3:

```text
A → D
B → E
C → F
```

Therefore:

```text
Hello, World!
```

becomes:

```text
Khoor, Zruog!
```

Characters that are not letters, such as spaces, numbers and punctuation, remain unchanged.

## Requirements

* Python 3
* Flask
* Gunicorn

## Installation

Clone the repository:

```bash
git clone https://github.com/BHASVIC-KAMSI25/CS_1_CaesarCipher_BYTE.git
```

Navigate into the project directory:

```bash
cd CS_1_CaesarCipher_BYTE
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

Start the Flask application:

```bash
python app.py
```

Open the local address shown in the terminal, normally:

```text
http://127.0.0.1:5000
```

## Usage Example

### Encryption

Input:

```text
Text: Hello, World!
Shift: 3
```

Output:

```text
Khoor, Zruog!
```

### Decryption

Input:

```text
Text: Khoor, Zruog!
Shift: 3
```

Output:

```text
Hello, World!
```

### Characters That Stay Unchanged

Input:

```text
Hello, World! 123
```

with a shift of `3` produces:

```text
Khoor, Zruog! 123
```

The spaces, punctuation and numbers remain unchanged.



## Deployment

The application can be deployed as a Python web service using Render.

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```

## Author
Kamsi Amandu-Ndubuisi For B.Y.T.E Cyber Security Internship

Task 1: Caesar Cipher
