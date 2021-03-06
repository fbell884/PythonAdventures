from random import randint 

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def generate_otp(sheets, length): 
   for sheet in range(sheets): 
      with open("otp" + str(sheet) + ".txt", "w") as f: 
         for i in range(length): 
            f.write(str(randint(0,26)) + "\n")

def load_sheet(filename): 
   with open(filename, "r") as f:
      contents = f.read().splitlines()
   return contents

def get_plaintext():
   plaintext = input('Please type your message ')
   return plaintext.lower()

def load_file(filename): 
   with open(filename, "r") as f: 
      contents = f.read()
   return contents


def save_file(filename, data): 
   with open(filename, "w") as f: 
      f.write(data)


def encrypt(plaintext, sheet): 
   ciphertext = ''
   for position, character in enumerate(plaintext): 
      if character not in ALPHABET: 
         ciphertext += character
      else: 
         encrypted = (ALPHABET.index(character) + int(sheet[position])) % 26
         ciphertext += ALPHABET[encrypted]
   return ciphertext


sheet = load_sheet('otp0.txt') 
encrypt('This is a secret message.', sheet) 


