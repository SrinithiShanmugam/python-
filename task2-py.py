#1.smallest between two numbers
a=int(input("enter num:"))
b=int(input("enter num:"))
if a>b :
    print(a ,"is greatrer")
else:
    print(b,"is greater")


#2.smallest among three numbers
a=int(input("enter num:"))
b=int(input("enter num:"))
c=int(input("enter num:"))
if a>b  and a>c:
    print(a ,"is greatrer")
elif b>a and b>c:
    print(b,"is greater")
else:
    print(c,"is greater")
    
#3.Absolute value
a=int(input("enter number"))
print(-(a))

#4.even or add
a=int(input("enter num:"))
if a%2==0:
    print("even")
else:
    print("odd")
    
#5.given number is a multiple of 5 or not.
a=int(input("enter num:"))
if(a%5==0):
    print("num is multiple of 5")
else:
      print("num is  not multiple of 5")

Book11.xlsx given number is a multiple of 10 or not

a=int(input("enter num:"))
if(a%10==0):
    print("num is multiple of 10")
else:
      print("num is  not multiple of 10")

#7.given number is a two-digit number or not.
a=int(input("enter num:"))
if(10<=a<=99):
    print(a,"is two digit")
else:
    print(a,"is not two digit")
    
#8given number is a three-digit number or not.
a=int(input("enter num:"))
if(100<=a<=999):
    print(a,"is three digit")
else:
    print(a,"is not three digit")
    
#9.given number ends with zero or not.
a=int(input("enter num:"))
if(a%10==0):
    print("num end with zero")
else:
      print("num is  not end with zero")


#10.program to accept a number and check if its square is above 50 or below 50.
a=int(input("enter num:"))
if(a**2<50):
    print(a ,"square is less than 50")
else:
    print(a ,"square is not less than 50")
    
#11.program to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not
a=int(input("enter num:"))
b=int(input("enter num:"))
if a-b==0:
    print("the difference is zero")
else:
    print("the difference is  not zero")
    
#12.The student has passed if marks is 50 or above otherwise failed).
mark=int(input("enter num:"))
if mark>=50:
    print("passed")
else:
    print("failed")
    
#13.program to accept a number and check if the number is divisible by 10.
a=int(input("enter num:"))
if(a%10==0):
    print(a,"is divisible by 10")
else:
     print(a,"is  not divisible by 10")
     
#14.program to take a two-digit number and print the biggest digit.
num = int(input("Enter a two-digit number: "))

first_digit = num // 10
second_digit = num % 10

if first_digit > second_digit:
    print("Biggest digit is:", first_digit)
else:
  print("Biggest digit is:", second_digit)
  
#15. If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult.
a=int(input("enter number"))
if a==1:
      print("exam easy")
else:
    print("exam will be difficult")
      
#16.If the value entered is 1 then print “You can go out and play” otherwise “You cannot go out and play"
a=int(input(" enter num"))
if a==1:
      print("You can go out and play")
else:
    print("You cannot go out and play")


#17.program to accept the length and breadth of a shape and print if they are the same. If they are the same, print it’s a square otherwise its rectangle.
len=int(input("enter num"))
bdh=int(input("enter num"))
if len==bdh:
    print("square")
else:
    print("rectangle")
    
#18.given number is the ASCII value of an uppercase alphabet or not.
a=int(input(" enter num"))
if 65<=a<90:
    print("ascii value upper")
else:
    print("ascii lower")
  
#19.given number is the ASCII value of a lowercase alphabet.
a=int(input(" enter num"))
if 97<=a<122:
    print("ascii value lower")
else:
    print("ascii upper")
   
#20.given number is the ASCII value of a numeric character or not.
a=int(input(" enter num"))
if 48<=a<57:
    print("ascii value num")
else:
    print("ascii not num")

#21.whether the given number is a multiple of both 5 and 3.
a=int(input("enter num"))
if a%5&3==0:
    print("multiple of both 5 and 3")
else:
    print(" not multiple of both 5 and 3")
    
#22.given number is a three-digit number and also a multiple of 10.
a=int(input("enter num"))
if  a>=100 and a<=999 and a%10==0:
    print("multiple of 10")
else:
    print("not multiple of 10")

#23.given number is a three-digit number and also a multiple of 2, 5, and 10.
a=int(input("enter num"))
if  a>=100 and a<=999 and a%10&2&5==0:
    print("multiple of 10,5,2")
else:
    print("not multiple of 10,5,2")

#24.If both numbers are even, find their product. Otherwise, find their sum.
a=int(input("enter num"))
b=int(input("enter num"))
if a%2==0 and b%2==0:
    print(a*b)
else:
    print(a+b)
  
#25.A number is said to be Buzz Number if it ends with 7 or is divisible by 7. Example: 1007 is a Buzz Number. Define a class Buzz number to read a number and check if it is a Buzz number or not.
num = int(input("Enter a number: "))

if num % 10 == 7 or num % 7 == 0:
    print("It is a Buzz Number")
else:
    print("It is NOT a Buzz Number")
'''
#If elif else
#1.Find the largest number among three integers
'''
a=int(input("enter num:"))
b=int(input("enter num:"))
c=int(input("enter num:"))
if a>b and a>c:
    print(a," is greater")
elif b>a and b>c:
    print(b,"is graeter")
else:
    print(c,"is greater")
    
#2.2.Find the smallest number among three integers.
a=int(input("enter num:"))
b=int(input("enter num:"))
c=int(input("enter num:"))
if a<b and a<c:
    print(a," is smaller")
elif b<a and b<c:
    print(b,"is smaller")
else:
    print(c,"is smaller")

#3.Check if a given number is greater than 0, if yes then print 'Positive'. If the given number is lesser than 0, then print 'Negative'. If the given number is exactly equal to 0, then print 'Zero'.
a=int(input("enter num:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
elif a==0:
    print("zero")
else :
    print("invalid")
   
#4.4.A library charges fine for books returned late. To calculate the fine, define a class Library with the following .To input the number of days books were returned late. To calculate and print the fine based on the following condition:
#a.First five days 40 paisa per day 
#b.Six to ten days 65 paisa per day 
#c.above 10 days 80 paisa per day
days = int(input("Enter number of days late: "))

if days <= 5:
    fine = days * 0.40
elif days <= 10:
    fine = (5 * 0.40) + (days - 5) * 0.65
else:
    fine = (5 * 0.40) + (5 * 0.65) + (days - 10) * 0.80

print("Total fine = ₹", fine)

#5.Write a  program that functions as a basic calculator. The program will prompt the user to input two numbers and a mathematical operation (+, -, x, /). It will then perform the selected operation and display the result on the screen.
a=int(input("enter value :"))
b=int(input("enter value:"))
ope=input("enter operator:")
if ope == '+':
    print(a+b)
elif ope == '-':
    print(a-b)
elif ope == '*':
    print(a*b)
elif ope == '/':
    print(a/b)
else :
    print("inavalid")

#6.Check whether the given number is a multiple of 5, 3, and 7.
a=int(input("enter value :"))
if a%5&3&7==0:
    print("number is a multiple of 5, 3, and 7")
else:
    print("number is  not a multiple of 5, 3, and 7")
    
#7.To input weight of the parcel and type of booking (`O' for ordinary and 'E' for express).To compute and display the charges based on the weight of the parcel as per the tariff given 
weight = int(input("Enter weight of parcel : "))
type = input("Enter type : ")

if type == 'O':
    if weight <= 100:
        charge = 80
    elif weight <= 500:
        charge = 150
    elif weight <= 1000:
        charge = 210
    else:
        charge = 250

elif type == 'E':
    if weight <= 100:
        charge = 100
    elif weight <= 500:
        charge = 200
    elif weight <= 1000:
        charge = 250
    else:
        charge = 300

else:
    print("Invalid type")
    charge = None

if charge != None:
    print("Total charge = ₹", charge)
    
#8.Write a program to compute the discount according to the given conditions for the purchase of laptop. to take the price of the laptop.to calculate the charge according to the following condition.
price = float(input("Enter laptop price: "))

if price <= 50000:
    discount = 0
elif price <= 100000:
    discount = price * 0.10
elif price <= 150000:
    discount = price * 0.15
else:
    discount = price * 0.20

final_price = price - discount

print("Discount = ₹", discount)
print("Amount to pay = ₹", final_price)
