#!/usr/bin/env python
# coding: utf-8
1. Create a function to perform basic arithmetic operations that includes
addition, subtraction, multiplication and division on a string number (e.g. "12 +
24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space
and 2. For the challenge, we are going to have only two numbers between 1
valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals
"0" return -1.
For example:
"15 // 0" ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0
arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
# In[188]:


import operator
def arithmetic_operation(string):
    """"""
    ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "//":operator.floordiv, "/":operator.truediv} 
    string = string.split()
    try:
        output= ops[string[1]](float(string[0]),float(string[2]))
    except ZeroDivisionError:
        output = -1
    except Exception as e:
        print("Exception occured : ",e)
    return output


arithmetic_operation("12 * 12")

2. Write a function that takes the coordinates of three points in the form of a
2d array and returns the perimeter of the triangle. The given points are the
vertices of a triangle on a two-dimensional plane.
Examples
perimeter( [ [15, 7], [5, 22], [11, 1] ] ) ➞ 47.08
perimeter( [ [0, 0], [0, 1], [1, 0] ] ) ➞ 3.42
perimeter( [ [-10, -10], [10, 10 ], [-10, 10] ] ) ➞ 68.28
# In[191]:


def perimeter(cordinates):
    """This function takes the coordinates of three points in the form of a 2d array and returns the perimeter 
    of the triangle."""
    A = cordinates[0]
    B = cordinates[1]
    C = cordinates[2]
    AB = m.sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
    BC = m.sqrt((B[0]-C[0])**2+(B[1]-C[1])**2)
    CA = m.sqrt((C[0]-A[0])**2+(C[1]-A[1])**2)
    perimeter = round(AB+BC+CA,2)
    return perimeter

print(perimeter([ [-10, -10], [10, 10 ], [-10, 10] ] ))

3. A city skyline can be represented as a 2-D list with 1s representing
buildings. In the example below, the height of the tallest building is 4 (second-
most right column).
[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the
height of the tallest skyscraper.
Examples
tallest_skyscraper([
[0, 0, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1]
]) ➞ 3
tallest_skyscraper([
[0, 1, 0, 0],
[0, 1, 0, 0],
[0, 1, 1, 0],
[1, 1, 1, 1]
]) ➞ 4
tallest_skyscraper([
[0, 0, 0, 0],
[0, 0, 0, 0],
[1, 1, 1, 0],
[1, 1, 1, 1]
]) ➞ 2
# In[121]:


import numpy as np
def tallest_skyscraper(heights):
    """This function takes a skyline (2-D list of 0's and 1's) and returns the
height of the tallest skyscraper"""
    arr = np.array(heights)
    output = arr[0]
    for i in range(len(arr)-1):
        output = output+arr[i+1]
    return max(output)
         
    

output = tallest_skyscraper([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]])

print(output)

4. A financial institution provides professional services to banks and claims
charges from the customers based on the number of man-days provided.
Internally, it has set a scheme to motivate and reward staff to meet and
exceed targeted billable utilization and revenues by paying a bonus for each
day claimed from customers in excess of a threshold target.
This quarterly scheme is calculated with a threshold target of 32 days per
quarter, and the incentive payment for each billable day in excess of such
threshold target is shown as follows:
Days Bonus
0 to 32 days Zero
33 to 40 days SGD$325 per billable day
41 to 48 days SGD$550 per billable day
Greater than 48 days SGD$600 per billable day

Please note that incentive payment is calculated progressively. As an
example, if an employee reached total billable days of 45 in a quarter, his/her
incentive payment is computed as follows:
32*0 + 8*325 + 5*550 = 5350
Write a function to read the billable days of an employee and return the bonus
he/she has obtained in that quarter.
Examples
bonus(15) ➞ 0
bonus(37) ➞ 1625
bonus(50) ➞ 8200
# In[190]:


def incentive_payment(days):
    """This function read the billable days of an employee and return the bonus
he/she has obtained in that quarter."""
    if days<=32:
        bonus=0
        return bonus 
    elif days<=40:
        bonus=32*0+(days-32)*325
        return bonus
    elif days<=48:
        bonus=32*0+(days-40)*550+8*325
        return bonus
    else:
        bonus=32*0+(days-48)*600+8*325+8*550
        return bonus
    
incentive_payment(37)

5. A number is said to be Disarium if the sum of its digits raised to their
respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32
is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(544) ➞ False
is_disarium(518) ➞ True
is_disarium(466) ➞ False
is_disarium(8) ➞ True
# In[189]:


def is_disarium(num):
    """This function determines whether a number is a Disarium or not."""
    tot=0
    for i, j in enumerate(str(num)):
        tot += int(j)**(i+1)
    if tot==num:
        return True
    else:
        return False

is_disarium(8)


# In[ ]:




