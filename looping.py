#Looping Statements

#1.Write a program to print the first N natural numbers. Input : 10 , Output : 1 2 3 4 5 6 7 8 9 10

'''n = int(input(enter num:))
for i in range(1, n + 1):
    print(i, end=" ")
    
#2.Write a program to print the first N even natural numbers. Input : 5 , Output 2 4 6 8 10
a=int(input("enter num:"))
for i in range(2,11,2):
    print(i)
    
#3.Write a program to print the first N odd natural numbers. Input : 5 , Output : 1 3 5 7 9
a=int(input("enter num:"))
for i in range(1,10,2):
    print(i)
    
#4.Write a program to print first N multiples of 3. Input : 7 , Output : 3 6 9 12 15 18 21
a=int(input("enter num:"))
for i in range(3,22,3):
    print(i)

#5.Write a program to print first N multiples of 5. Input : 5 , Output : 5 10 15 20 25
a=int(input("enter num:"))
for i in range(5,26,5):
    print(i)

#6.Write a program to print all the multiples of 2 till N. Input : 15 , Output : 2 4 6 8 10 12 14
a=int(input("enter num:"))
for i in range(2,15,2):
    print(i)
    
#7.Write a program to print all the numbers which are multiples of either 2 or 3 till N. Input : 15 , Output : 2 3 4 6 8 9 10 12 14 15
a=int(input("enter num:"))
for i in range(2,a+1):
    if i%2==0 or i%3==0:
       print(i)
       
#8.Write a program to print all the numbers which are multiples of either 2, 5 or 7 till N. Input : 15 , Output : 2 4 5 6 7 8 10 12 14 15
a=int(input("enter num:"))
for i in range(2,a+1):
    if i%2==0 or i%5==0 or i%7==0:
       print(i)
       
#9.Write a program to print the first N multiples of either 3, 5 or 7.Input : 10 , Output : 3 5 6 7 9 10 12 14 15 18
a=int(input("enter num:"))
for i in range(3,a+1):
    if i%3==0 or i%5==0 or i%7==0:
       print(i)'''
#Find the sum of all digits in a positive integer. Input : 123456789
i=0
while i<10:
    i=i+
