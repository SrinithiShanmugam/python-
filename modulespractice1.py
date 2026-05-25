'''

PREDEFINED MODULES 


#random
import random as r
print(r.random())

print(r.randint(1,50))
print(r.randrange(0,100,15))

#sys module
import sys as s
a=dir(s)
print(a)
print("-----------------------------------------")
print(s.path)
print("---------------------------------------")
print(s.version)


#Socket module
import socket
host=socket.gethostname()
print(host)

# pywhatkit modul
e(
img in browsert)(install within the script of cmd)

import pywhatkit
pywhatkit.search("Rohit sharma")

#web browser module
import webbrowser
webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Rohit_Sharma")


# calender module
import calendar as c
#print(c.month(2004,9))
#print(c.isleap(2024))
print(c.calendar(2025))

#time module
import time
print(time.ctime())
print("hii")
time.sleep(3)
print("hello sri")

import time(ex-time sleep)
for i in range(1,6,1):
    print(i)
    time.sleep(2)

#turtle module
import turtle
square = turtle.Turtle()
square.right(80)
square.forward(80)
for i in range(4):
    square.right(70)
    square.forward(65)
turtle.done()

#numpy module
import numpy as n
a=n.array([1,2,3,4,5])
print(a)
print(n.min(a))
print(n.shape(a))
print(n.max(a))
print(n.sqrt(a))
print(n.mean(a))
print(n.median(a))


#examples
import numpy as s
a=s.array([1,2,3])
print(a[0])
print(a)
print(s.sort(a))
print(s.max(a))#( is string  placed mean no output)

#matplotlib
import matplotlib.pyplot as plt
import numpy as np
# Students' height and weight
height = np.array([150,120,145,205,234,543,111])
weight = np.array([45, 50, 55, 60, 65, 72, 78])
plt.plot(weight,height, color='blue')
plt.title('Height vs Weight of Students')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

#matplotlib plot
import matplotlib.pyplot as plt
import numpy as np
# Sales data
products = np.array(['Laptops', 'Mobiles', 'Tablets', 'Headphones'])
sales = np.array([250, 400, 150, 300])
plt.bar(products, sales, color='orange')
plt.title('Sales by Product')
plt.xlabel('Products')
plt.ylabel('Units Sold')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
# Students marks
marks = np.random.randint(40, 100, 100)
plt.hist(marks, bins=10, color='purple', edgecolor='black')
plt.title("Distribution of Students' Marks")
plt.xlabel('Marks Range')
plt.ylabel('Number of Students')
plt.show()

import matplotlib.pyplot as plt
import numpy as np
# Market share
companies = ['Apple', 'Samsung', 'Xiaomi', 'Others']
market_share = np.array([30, 25, 20, 25])
plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=90)
plt.title('Mobile Market Share')
plt.show()
'''

