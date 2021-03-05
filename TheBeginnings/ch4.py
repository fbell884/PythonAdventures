# 1 

number = 0
count = 0
total = 0
avg = 0
done = 'done'

while number != done: 
   number = input("Please enter a number")
   if number != done:
      number = int(number) 
      total += number
      count += 1
      avg = total/count
   else: 
      break

print("Total = " + str(total) + "\nCount = " + str(count) + "\nAverage " + str(avg))

