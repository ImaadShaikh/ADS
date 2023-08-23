from Method import *

assert(largest_number([10,20,30,90])==90)
assert(Second_largest_number([10,30,2,5])==10)
assert(odd_even([0, 2, 4, 6, 8,1,3,5])==([1,3,5],[0,2,4,6,8]))
assert(same_list([1,2,3,4,5],[1,3,4,5,2])==True)
assert(union([1,2,3,4],[1,3,4,5,6])==[1,2,3,4,1,3,4,5,6])
assert(intersection([1,2,3],[1,2,4,5])==[1,2])
assert(unionIntersection([1,2,3,5],[1,2,4,6,8])==({1,2,3,5,4,6,8},{1,2}))
assert(tuplelist(4)==[(1,1),(2,4),(3,9),(4,16)])
assert(Duplicate_items([1,1,2,3,4,5,5,7,8])=={1,2,3,4,5,7,8})
assert(longest_word(["Imaad","shaikh","book"])==6)
assert(addKeyValue({"a":"imaad","n":"isra"},"j","Bike")==({"a":"imaad","n":"isra","j":"Bike"}))
assert(merge({"a":"imaad",1:"shawarma"},{"b":"uae","c":"gulf"})==({"a":"imaad",1:"shawarma","b":"uae","c":"gulf"}))
assert(to_check({1:1,2:4,3:9},6)==False)
assert(square_no((4)==({1:1,2:4,3:9,4:16})))
assert(sum_keys(({1:1,2:4,3:9}))==14)
assert(multiply_keys({1:1,2:4,3:9})==36)
assert(delete_key({1:1,2:4,3:9},2)==({1:1,3:9}))
assert(is_empty(({}))==True)
assert(create_new(((1,9),(2,7)))==({1:9,2:7}))
dict = {'e': 'u', 'b': 's', 'k': 'x', 'u': 'q', 'y':
'c', 'm': 'w', 'o': 'y', 'g': 'f', 'a': 'm', 'x': 'j', 'l': 'n', 's':
'o', 'r': 'g', 'i': 'i', 'j': 'z', 'c': 'k', 'f': 'p', ' ': 'b', 'q':
'r', 'z': 'e', 'p': 'v', 'v': 'l', 'h': 'h', 'd': 'd', 'n': 'a', 't':
' ', 'w': 't'}
assert(encryption(dict,"cat")==("km ")) 