print("*******Digits Sum of a Number*******")



num = int(input("Enter a number: "))
try:
   if num > 10:
       sm = 0
       while num > 0:
           d = num%10
           num = num//10
           sm += d
           print("The sum of digits of number is",sm)
except:
   raise print("Enter two digit number!!!")