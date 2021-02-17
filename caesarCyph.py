# Learning encryption techniques

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = input('Enter a number for your key: ')
newMsg = ''

key = int(key)

message = input('Please enter a message: ')

for character in message: 
   if character in alphabet: 
      position = alphabet.find(character)
      newPosition = (position + key) % 26

      newCharacter = alphabet[newPosition]
      newMsg += newCharacter
   else: 
      newMsg += character

print('The new message is:', newMsg)




