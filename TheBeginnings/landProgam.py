def say_hi(name): 
   if name == ' ':
      print('You did not enter your name!')
   else:
      print("Hi there... ")
      for letter in name: 
         print(letter) 

name = input("Enter your name")

say_hi(name)
