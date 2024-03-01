# Data structure 
## list
اما ordered ------mutable اقدر اوصل له عن طريق الindex ارقام... و متغير اقدر اغير اى عنصر زى الlist []  
list is a data structure that allows you to store and manipulate a collection of items. Lists are mutable, which means you can change their content after they are created. They are very versatile and commonly used in Python programming.

Here's a breakdown of lists and their types, along with examples and commonly used functions:

### 1. List Basics:
A list in Python is defined by enclosing comma-separated values within square brackets `[ ]`.

```python
my_list = [1, 2, 3, 4, 5]
```
### 2. Types of Lists:
   - **Homogeneous Lists:** Contains elements of the same data type.like array
   - **Heterogeneous Lists:** Contains elements of different data types.

```python
homogeneous_list = [1, 2, 3, 4, 5]
heterogeneous_list = [1, 'two', 3.0, True]
```

### 3. Common List Operations and Functions:
   - **Accessing Elements:**
   

```python 
   print(my_list[0])  # Accessing the first element (indexing starts from 0)
    print(my_list[-1]) # Accessing the last element
    print(my_list[1:3])  # Slicing from index 1 to 2 (exclusive)
    my_list.append(6)  # Appends 6 to the end of the list
    my_list.insert(2, 'inserted')  # Inserts 'inserted' at index 2
    my_list.extend([6, 7, 8])  # Appends multiple elements to the end of the list
    my_list.remove(3)  # Removes the first occurrence of 3 value 
    my_list.clear()  # Removes all elements from the list
    del my_list[2]  # Deletes the element at index 2 from the list
    popped_element = my_list.pop()  # Removes and returns the last element and we can give it index
    print(len(my_list))  # Returns the number of elements in the list
    my_list.sort()  # Sorts the list in ascending order in the origion list itself
    sorted_list = sorted(my_list)   # Returns a new sorted list.
    sorted_by_second = sorted(<collection of tuples>, key=lambda el: el[1])
    sorted_by_both   = sorted(<collection of tuples>, key=lambda el: (el[1], el[0]))
    my_list.reverse()  # Reverses the elements of the list
    reversed_list = my_list[::-1]  # Reverses the list using slicing
    concatenated_list = my_list + [7, 8, 9]
    count = my_list.count(2)  # Returns the number of occurrences of 2 value in the list
    index = my_list.index(3)  # Returns the index of the first occurrence of 3
    is_present = 3 in my_list  # Returns True if 3 is present in the list, False otherwise
    copied_list = my_list.copy()  # Creates a shallow copy of the list
    any_true = any([False, True, False])  # Returns True if any element in the list is True
    all_true = all([True, True, True])    # Returns True if all elements in the list are True
    unique_elements = list(set(my_list))  # Removes duplicates by converting list to set and back to list

    txt = "apple#banana#cherry#orange"
    x = txt.split("#", 1)         # setting the maxsplit parameter to 1, will return a list with 2 elements! [apple, banana#cherry#orange]
    # Example of split method
    sentence = "I love eating fruits like apple, banana, and orange"
    word_list = sentence.split()
    print(word_list)
    # Output: ['I', 'love', 'eating', 'fruits', 'like', 'apple,', 'banana,', 'and', 'orange']
    # Example of join method
    words = ["apple", "banana", "orange", "grape"]
    joined_string = ", ".join(words)
    print(joined_string)
    # Output: "apple, banana, orange, grape"


    letters = ['a', 'b', 'c']
    numbers = [1, 2]
    zipped = list(zip(letters, numbers))  # Combines elements from both lists into tuples  [('a',1),('b',2)]
    
    # Unpacking
    listt= [1,2,3,4,5]  # Unpacking list must be the same number of the list
    frist,second,*remain=listt
    print(frist,second,remain)
    # Output >> 1 2 [3, 4, 5]
    #we can use unpacking operator to make list or combine two list in the new list
    First=[1,2]
    Second=[3,4,5]
    values =[*first, "a", *second]
    print(values)
    # >> Output= [1,2,"a",3,4,5]

    #enumerate() ->it add counter for iterable when making for loop
    for index, value in enumerate(my_list):  # Iterates over each element with its index  ((0,'a'),(1,'b')...)
        print(index, value)             
.   #it also delete the elements from enumerate tuples not the object as it fetch all element for the variable
    l1= ['ahmed', 10, 333.33, 'mina', True]
    l1_enum = enumerate(l1)
    for abbass, test in l1_enum:
        print(f"{abbass} : {test}")
    # # cast enum to alist
    items =list(l1_enum)
    print(items) # it will be empty
    

    filtered_list = list(filter(lambda x: x % 2 == 0, my_list))  # Filters elements based on a condition
    mapped_list = list(map(lambda x: x * 2, my_list))  # Applies a function to each element of the list
    from functools import reduce
    reduced_value = reduce(lambda x, y: x + y, my_list)  # Reduces the list to a single value using a function

    squares = [x**2 for x in range(10)]  # Creates a list of squares of numbers from 0 to 9
    evens = [x for x in my_list if x % 2 == 0]  # Creates a list of even numbers from my_list
    doubled = [x * 2 for x in my_list]  # Creates a list by doubling each element of my_list
    
```

----------
## tuple 

اما ordered ---------immutable مش متغير ما اقدرش اعدل عليه زى الmy_tuple =1,4 
ملحوظه ينفع اعدل قيمه للlist جوه الtuple () وال string برددو

so i can't insert on it or append or delete
### What is a Tuple?

A tuple in Python is similar to a list, but with one key difference: it's immutable. This means that once a tuple is created, its elements cannot be changed, added, or removed. Tuples are defined by enclosing comma-separated values within parentheses `( )`.

### Tuple Creation:
```python
my_tuple = (1, 2, 3, 4, 5)
```

### Types of Tuples:
   - **Homogeneous Tuples:** Contains elements of the same data type.
   - **Heterogeneous Tuples:** Contains elements of different data types.

```python
homogeneous_tuple = (1, 2, 3, 4, 5)
heterogeneous_tuple = (1, 'two', 3.0, True)
```

```python
# Accessing Elements
print(my_tuple[0])   # Accessing the first element (indexing starts from 0)
print(my_tuple[-1])  # Accessing the last element

# Tuple Slicing
print(my_tuple[1:3])  # Slicing from index 1 to 2 (exclusive)

# Tuple Operations
concatenated_tuple = my_tuple + (6, 7, 8)  # Concatenating Tuples
repeated_tuple = my_tuple * 3             # Repeating Tuples

# Common Tuple Functions and Methods
print(len(my_tuple))                  # Length of Tuple
count = my_tuple.count(2)             # Counting Occurrences
index = my_tuple.index(3)             # Finding Index
packed_tuple = 1, 2, 3                # Tuple Packing
a, b, c = packed_tuple                # Tuple Unpacking
# swapping two variable using tuple 
a=10 , b=12          
b,a= a,b                           
list_from_tuple = list(my_tuple)      # Tuple Conversion
combined_tuple = my_tuple + another_tuple  # Combining Tuples

# Additional Techniques and Functions
sorted_tuple = tuple(sorted(my_tuple))  # Tuple Sorting
is_present = 3 in my_tuple              # Membership Testing
copied_tuple = my_tuple[:]              # Copying Tuples
max_value = max(my_tuple)                  # Finding Maximum
min_value = min(my_tuple)                  # Finding Minimum
nested_tuple = ((1, 2), (3, 4), (5, 6))
flattened_tuple = tuple(item for sublist in nested_tuple for item in sublist)  # Flattening Nested Tuples
a, *rest = my_tuple                        # Tuple Unpacking with Asterisk
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
tuple_of_lists = tuple(zip(*list_of_tuples))  # Converting List of Tuples to Tuple of Lists

for index, value in enumerate(my_tuple):  # Enumerating Tuples
    print(index, value)
```

---------
## set 
اما unordered ---------mutable الset {} مفيش فيها تكرار تنفع لو ارقام تليفونات ولانها بتظهر عشوائى فى كل مره ينفع استخدمها فى عرض اسأله امتحان مثلا it take only the immutable elements as it hash every element

### What is a Set?

A set in Python is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements, but the elements themselves must be immutable (e.g., numbers, strings, tuples). Sets are defined by enclosing comma-separated elements within curly braces `{ }`.

### Set Creation:
```python
my_set = {1, 2, 3, 4, 5}
```

### Types of Sets:
   - **Mutable Sets:** You can add or remove elements from these sets.
   - **Immutable Sets (Frozensets):** Once created, the elements cannot be changed.
```python
   # Types of Sets
mutable_set = {1, 2, 3}
immutable_set = frozenset({4, 5, 6})
```

```python
# Set Operations
union_set = my_set.union(mutable_set) # we can make it using this operator |
intersection_set = my_set.intersection(mutable_set) # we can make it using this operator &
difference_set = my_set.difference(mutable_set)       # we can make it using this operator -
symmetric_difference_set = my_set.symmetric_difference(mutable_set)      # we can make it using this operator ^
my_set |= mutable_set  # Updates my_set with the union of itself and mutable_set
my_set &= mutable_set  # Updates my_set with the intersection of itself and mutable_set
my_set -= mutable_set  # Updates my_set with the difference between itself and mutable_set
my_set ^= mutable_set  # Updates my_set with the symmetric difference between itself and mutable_set
equal_sets = my_set == mutable_set  # Checks if my_set and mutable_set contain the same elements

is_subset = my_set.issubset(mutable_set)  # Checks if my_set is a subset of mutable_set
is_superset = my_set.issuperset(mutable_set)  # Checks if my_set is a superset of mutable_set
is_disjoint = my_set.isdisjoint(mutable_set)  # Checks if my_set and mutable_set have no common elements

# Adding Elements
my_set.add(6)   # it add one element 
my_set.update({7, 8, 9})# it add more than one element

# Removing Elements
my_set.remove(3)  # Removes the element 3 from the set, raises KeyError if element doesn't exist
my_set.discard(10)  # Removes the element 10 from the set if it exists, otherwise does nothing
my_set.clear()  # Removes all elements from the set, making it empty

# Checking Membership
is_present = 3 in my_set  # Checks if the element 3 is present in the set

# Copying a Set
copied_set = my_set.copy()  # Creates a shallow copy of the set

# Additional Set Functions and Methods
print(len(my_set))  # Prints the number of elements in the set
set_from_list = set([1, 2, 3, 4, 5])  # Creates a set from a list
tuple_list = [(1, 2), (3, 4), (5, 6)]  # List of tuples
tuple_set = set(tuple_list)  # Creates a set from a list of tuples

list_from_set = list(my_set)  # Converts the set to a list
my_set.difference_update({3, 4, 5})  # Removes elements {3, 4, 5} from my_set
my_set.symmetric_difference_update(mutable_set)  # Updates my_set with the symmetric difference between itself and mutable_set

cartesian_product_set = {(x, y) for x in range(3) for y in range(3)}  # Creates a set of tuples representing the Cartesian product

# Set Comprehensions
squared_set = {x**2 for x in range(10)}  # Creates a set containing the squares of numbers from 0 to 9

```
------
# Dictonary 
الdictionary ..طلعت immutable اقدر اعدل فى الvalue ما اقدرش اعدل فى الkey و unordered


```python 
# Dictionary Creation
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Accessing Values
value = my_dict['key1']  # Accessing the value associated with 'key1'

# Adding and Modifying Elements
my_dict['new_key'] = 'new_value'  # Adding a new key-value pair
my_dict['key1'] = 'updated_value'  # Modifying an existing value

# Removing Elements
del my_dict['key2']  # Deleting a key-value pair by key
my_dict.pop('key3')  # Removing a key-value pair by key 
my_dict.clear()      # Removing all key-value pairs from the dictionary

# Dictionary Methods
keys = my_dict.keys()     # Returns a view of keys in the dictionary as list
values = my_dict.values() # Returns a view of values in the dictionary as list
items = my_dict.items()   # Returns a view of key-value pairs (tuples) in the dictionary
copied_dict = my_dict.copy()  # Creates a shallow copy of the dictionary
other_dict = {'key4': 'value4', 'key5': 'value5'}
my_dict.update(other_dict)    # Merges other_dict into my_dict, overwriting existing keys

#unpacking example
myUltimateSkills ={"HTML":{"Main":"80%","Pugjs":"80%"},
"CSS":{"Main":"90%","Sass":"70%"}}
for main_key,main_value in myUltimateSkills.items(): #.items it get all dict items in tuple like ("HTML",{"Main":"80%","Pugjs":"80%"})
    print(f"{main_key} Progress Is: ")
    for child_key,child_value in main_value.items():
    print(f"- {child_key} => {child_value}")
## unpacking dict operator 
    First={'x':1,}
    Second={'x':5,"y":4}
    my_dict =[**first, "z":3 , **second]
    print(my_dict)
    Output= {'x':5,"y":4,"z":3}


# Additional Dictionary Functions
length = len(my_dict)   # Returns the number of key-value pairs in the dictionary
is_present = 'key1' in my_dict   # Returns True if 'key1' is present in the dictionary
value = my_dict.get('key', 'default_value')  # Returns the value for 'key' if it exists, otherwise returns 'default_value'
#join
myDict{"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
# More Advanced Techniques and Functions
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))  # Creates a dictionary from two lists

#group by
from collections import ChainMap, defaultdict
# Define your data here (list of tuples)
data = [('key1', 'value1'), ('key2', 'value2'), ('key1', 'value3'), ('key2', 'value4')]
# Create a defaultdict to map keys to multiple values
multi_dict = defaultdict(list)
# Populate multi_dict with data
for k, v in data:
    multi_dict[k].append(v)
# Print the resulting multi_dict
print("Multi Dictionary:", multi_dict)


merged_dict = dict(ChainMap(dict1, dict2))  # Merges dictionaries while preserving original dictionaries
# Dictionary Comprehensions
squared_dict = {x: x**2 for x in range(1, 6)}  # Creates a dictionary of squares from 1 to 5
inverted_dict = {v: k for k, v in my_dict.items()}  # Creates a new dictionary with keys as values and values as keys
merged_dict = {k: v for d in list_of_dicts for k, v in d.items()}  # Creates a dictionary by merging keys and values from a list of dictionaries
filtered_dict = {k: v for k, v in my_dict.items() if v != 'value_to_remove'}  # Removes key-value pairs with a specific value from the dictionary
```
-----
## map, filter ,reduce , comperhensive list and dictonry , generator 


----
## files 
#r r+(can read and write)  w(when w it delete everything) w+() a()   a+()


```python 
files= open("test.txt","a+")          if it doesn't exist it will create the file when you write or append
print(files.read())
print(files.write("omar"))
files.close()

With open('another_file.txt','r') as f:  #it will close the file after reading it
    File_data = f.read()

 So, essentially, the code reads all the PDF files from the specified directory, converts each file to HTML format, and saves the HTML output in a file with the same name as the PDF file but with an extension of ".html".
    
directory = "D:\\courses\\project_atom\\"#
pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
for pdf_file in pdf_files:
    text = convert_pdf(f"D:\\courses\\project_atom\\{pdf_file}","html","utf-8")
    with open(f'{pdf_file}.html',"w", encoding="utf-8") as f:
    f.write(text)

```
### jason
Json : it coud be all object into on list or one object contain list of object.   
1- To read a JSON file, you can use the json.load() function.This function reads a file-like object and returns the data. If you have a JSON string, you can parse it by using the json.loads() method. ( Json string parse to python object.)
```python
    Import json
    with open('data.json') as f :
        data =json.load(f)
```
2- To write data to a JSON file, you can use the json.dump() function. This function writes Python data to a file-like object. (convert python object to Json string)
     
```python
    data ={'name':'John','age':30,'city':'New York'}
    with open('users.json','w') as f:
        json.dump(data,f)
        
    data_json =json.dumps(data)
    with open('users.json','w') as f:
        f.write(data_json)
 ```
