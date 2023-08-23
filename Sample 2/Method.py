#1 Python Program to Find the Largest Number in a List
def largest_number(n):
    n.sort()
    return n[-1]
#2 Python Program to Find the Second Largest Number in a List
def Second_largest_number(n):
    n.sort()
    return n[-2]
#3 Python Program to Put Even and Odd elements in a List into Two Different Lists.
def odd_even(n):
    odd_num = []
    even_num =[]
    for i in range(len(n)):
        if n[i]%2 == 0:
            even_num.append(n[i])
        else:
            odd_num.append(n[i])
    return odd_num,even_num
#4 Python Program to check whether two lists are same.
def same_list(n,m):
    if (len(n)==len(m)):
        for i in n:
            f =0
            c = n.count(i)
            if i not in m or m.count(i) !=c:
                f = 1
                break
        if (f==1):
            return False
        else:
            return True
    else:
        return False
#5 Python Program to Find the Union of Lists.
def union(a,b):
    c = []
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    return c
#6 Python Program to find the Intersection of Lists.
def intersection(a,b):
    c = []
    for i in a:
        if i in b :
            c.append(i)
    return c
#7 Python Program to find union and intersection of lists without repetition
def unionIntersection(a,b):
    union_list = set(union(a,b))
    intersection_list = set(intersection(a,b))
    return union_list,intersection_list
#8 Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number.
def tuplelist(n):
    b = []
    for i in range(1,n+1):
        b.append((i,i**2))
    return b
#9 Python Program to Remove the Duplicate Items from a List.
def Duplicate_items(n):
    return set(n)
#10 Python Program to Read a List of Words and Return the Length of the Longest One.
def longest_word(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word) 
    return max_length 

#11 Python Program to Add a Key-Value Pair to the Dictionary
def addKeyValue(dictionary, key, value):
    dictionary[key] = value
    return dictionary
#12 Python Program to concatenate 2 dictionaries
def merge(dict1,dict2):
    concat_value = {**dict1,**dict2}
    return concat_value
#13 #Program to check if key exists in dictionary
def to_check(dict,key):
    if key in dict:
        return True
    else:
        return False
#14 Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form 
def square_no(n):
    dict = {}
    for i in (1,n+1):
        dict[i] = n*n
    return dict
#15 
def sum_keys(my_dict):
    total = sum(my_dict.values())
    return total
#16 
def multiply_keys(my_dict):
    answer = 1
    for i in my_dict:
        answer = answer*my_dict[i]
    return answer
#17
def delete_key(dict,key):
    if key in dict:
        del dict[key]
    return dict
#18
def is_empty(my_dict):
    return not bool(my_dict)
#19 
def create_new(tuple):
    dict = {}
    for key,value in tuple:
        dict[key] = value
    return dict
#20
def encryption(dict,a):
    encryption_items = a
    for key,value in dict.items():
        encryption_items = encryption_items.replace(key,value)
    return encryption_items


