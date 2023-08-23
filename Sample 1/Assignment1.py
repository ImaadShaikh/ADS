import random

#1 Python Program to swap numbers without using temp variable
def swap(x,y):
  x , y = y,x
  return x,y
#2 Python Program to Check Whether a Number is Positive or Negative.
#n = int(input("Enter"))
def positivenum(n):
  if n>-1:
   return positivenum
#3 Python Program to Print all Numbers in a Range Divisible by a Given Number. [ ifrange is from 1 to 20 and number is 4, then the result should be 4, 8, 12, 16 and 20. ]
def divisible(lim,n):
  list = []
  for i in range(1, 1+lim):
    if i%4 ==0:
      list.append(i)
  return list
#4 Python Program to Read Two Numbers and Print Their Quotient and Remainder.
#divisor = int(input("Enter divisor"))
#dividend = int(input("Enter value"))
#remainder = divisor % dividend
#print(remainder)

def divide(a,b):
  remainder = a%b
  quoitent =  a/b
  return remainder , quoitent
#5 Python Program to Print Odd Numbers Within a Given Range.
def oddnum(n):
  num = []
  for i in range(1,n):
    if i%2 != 0:
      num.append(i)
  return num
#6 Python Program to Find the Sum of Digits in a Number.
def sumofdigits(n):
  sum = 0
  while(n>0):
    r = n%10
    sum = sum + r
    n = int(n/10)
  return sum 
#7 Python Program to Find the Smallest Divisor of an Integer.
def smallestdivisor(n):
  for i in range(2,n-1):
    if i%2 ==0:
      return i
#8
def seriesofdigits(n):
  sum =0
  value = n
  some = 0
  while(n>0):
    sum = sum + some*10 + value
    some=some*10 + value
    n = n-1
    #print(sum)
  return sum

#9
def reversedigit(n):
  reverse = 0
  while(n>0):
    reverse = reverse*10+n%10
    n = int(n/10)
    #print(reverse)
  return reverse 
#10
def averagenumber(a):
  sum = 0
  for i in range(len(a)):
    sum = sum + a[i]
    average = sum/len(a)
    #print(average)
  return average 
#11Python Program to Count the Number of Digits in a Number.
def countnumber(n):
  count = 0
  while(n>0):
    count = count +1
    print(count)
    n = int(n/10)
  return count 
#12 Python Program to Check if a Number is a Palindrome.
def palinum(n):
  #reverse = n
  sum = 0 
  while(n>0):
    sum = sum *10 + int(n%10)
    n = int(n/10)
    print(sum)
  #return (reverse == sum)
  return sum
#13 Python Program to print the number of occurrence of a sub string in a given string.
def occurencenum(a,b):
  c = 0
  for i in range(len(a)):
   if (a[i:len(b)]==b):
     c = c+1
  return c
  

#14 Python program to print the lowest index in the string where substringsub is found within the string
#15 Python Program to return true if all characters in the string are alphabetic and there is at least one other character, False. 
#16 Python Program to Replace all Occurrences of ‘a’ with $ in a String.
def replace_value(a):
  modified_value = a.replace("a","$").replace("A","$").lower()
  print(modified_value)
  return modified_value
#17 Python Program to Count the Number of Vowels in a String
def no_of_vowels(n):
  c = 0
  for i in range(len(n)):
    if (n[i] in ['a','e','i','o','u','A','E','I','O','U']):
      c= c+1
      print(c)
  return c
#18 Program to replace blank space with a '-'
def replace_input(a):
  modified_value = a.replace(" ","-")
  print(modified_value)
  return modified_value
#19 Python Program to find the length of string without using any built-in functions.
#string = input("Enter string")
#count = 0
#for i in string:
  count = count +1
#print("The count is",count)
def length_string(a):
  if (a==''):
    return 0
  else:
   return 1+length_string(a[1:])
#20 Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.
def larger_string(a,b):
  n = (a)
  m = (b)
  if (n > m) :
    return(a)
  elif (n < m):
    return(b)
  else:
    return ("The string is equal")
#21 Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.
def Count_Upperlower(a):
  lower = 0 
  upper = 0
  for i in range(len(a)):
    if (a[i].islower()):
      lower = lower +1
    elif (a[i].isupper()):
      upper = upper + 1
  return lower,upper
#22 Python Program to Calculate the Number of Digits and Letters in a String.
def No_ofdigitsletter(n):
  if (64<ord(n)<90 or 96<ord(n)<121):
    return True
  else:
    return False
def counting_digits_chars(m):
  c =0
  d = 0
  for i in range(len(m)):
    if (No_ofdigitsletter(m[i])):
      c = c +1
      print(c)
    else:
      d = d+1
      print(d)
  return c , d

#23#Program to find if full pattern is present in a string
def full_pattern(a,b):
  if (b in a):
    return True
  else:
    return False
#24 Cumulative sum of a list [1, 2, 4, ...] is defined as[1, 3, 7, . . .]Write a functioncumulative_sum() to compute cumulative sum of a list
def cumulative_sum(a):
  sum = 0
  b = []
  for i in range(len(a)):
    sum = sum + a[i]
    b.append(sum)
    print(sum)
  return b
#25 Write a program to generate 10 random integers.
def tenrandomvalue():
  my_list=[]
  for i in range (10):
    value = random.randint(1,10)
    my_list.append(value)
  return my_list
#26 Write a program to generate 10 random integers between 1 to 20 
def randomintegers():
  my_list = []
  for i in range(10):
    value = random.randint(1,20)
    my_list.append(value)
  return my_list
#27 Write a program to generate 5 random integers between 1 to 20 such that numbers should be unique
def uniquevalues():
  my_list=set()
  for i in range(5):
    my_list.add(random.randint(1,20))
  return my_list
#28 Write a program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.
def randomvalues():
  my_list=[]
  n = 1
  for i in range(n,n+10):
    my_list.append(random.randint(1,100))
    n=n+10
  #print(n)
  #print(my_list)
  return my_list
