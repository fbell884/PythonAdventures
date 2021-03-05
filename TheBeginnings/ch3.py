# 1 & 2

try: 
   hrs_worked = float(input("Enter hours worked: "))
   pay_rate = float(input("Enter pay rate: "))
   fulltime = 40

   if hrs_worked > fulltime: 
      overtime = (hrs_worked - fulltime)
      otpay = 1.5 * pay_rate
      pay = (fulltime * pay_rate) + (overtime * otpay)
      print("\nYour pay is: $" + str(pay))
   else: 
      pay = hrs_worked * pay_rate 
      print("\nYour pay is: $" + str(pay))
except: 
    print("Please enter a number")


# 3

score = float(input("Enter your score "))

if score == 1.0:
   print("Congrats on your perfect score!")
elif score >= 0.9: 
  print("A")
elif score >= 0.8:
  print("B")
elif score >= 0.7: 
  print("C")
elif score >= 0.6: 
  print("D")
elif score < 0.6 and score > 0.0: 
  print("F")
else:
  print("Please enter a score within the ranges of 0.0 and 1.0")

