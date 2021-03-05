# Python for Everyone Chapter 2 Excercises

# 2

name = input("Please enter your name: ")

print("Howdy " + name + "!\n")

# 3

hours_worked = int(input("How many hours did you work this week? "))
pay_rate = float(input("What is your pay rate? "))
pay = hours_worked * pay_rate

print("\nThis weeks pay is: $" + str(pay) + "\n")


# 4 Finding the type 

width = 17
height = 12.0

print(type(width//2))
print(type(width/2.0))
print(type(height/3) + "\n") 


#5 F to C 

celsius = float(input("What is the temperature in Celsius? "))
converter = 9/5

fahren = celsius * 9/5 + 32

print("The converted temp is " + str(fahren) + "*F")
