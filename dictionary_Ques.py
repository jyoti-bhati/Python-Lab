
#Create a Dictionary:
numbers = [1, 2, 3, 4, 5]
cubes = {x: x ** 3 for x in numbers}
print(numbers)
print(cubes)



#Access and Modify a Dictionary:
student = {'name': 'John', 'age': 22, 'grade': 'A'}
print("Student Name: ",student['name'])

student['grade']='A+'
print(" Update Student Dictionary : ",student)



#Add and Remove Key-Value Pairs:
inventory = {'apples': 10, 'bananas': 5}
print(inventory )

inventory['oranges'] = 7
print(inventory )

del inventory['bananas']
print(inventory )



#Check for Key Presence:
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 88}
print("Is David in Scores? ",'David' in scores)



#Iterate Over a Dictionary:
for key, value in scores.items():
    print(f"{key}: {value}")


#Merge Two Dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged={**dict1, **dict2}
print("Merged Dictionaries",merged)


#Dictionary Comprehension

#Squares of Numbers:
squares = {num: num ** 2 for num in range(1, 11)}
print(squares)

#Filter Even Numbers:
even_squares = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}
print(even_squares)  


#Reverse a Dictionary:
original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {value: key for key, value in original_dict.items()}
print(reversed_dict)


#Count Character Frequency:
string = "programming"
char_count = {char: string.count(char) for char in string}
print(char_count)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


#Nested Dictionary:
nested_dict = {i: {j:i*j for j in range(1,4) }for i in range(1,4)}
print(nested_dict )

#Zip Two Lists into a Dictionary:
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
zipped_dict = {k: v for k, v in zip(keys, values)}
print("Zipped Dictionary:", zipped_dict)



#Filter Dictionary by Value:
marks = {'Alice': 85, 'Bob': 65, 'Charlie': 90, 'David': 72}
filtered_marks = {k: v for k, v in marks.items() if v > 80}
print("Filtered Dictionary:", filtered_marks)


# Multiplication table for 5
multiplication_table = {i: 5 * i for i in range(1, 11)}
print("Multiplication Table:", multiplication_table)



#Convert list of tuples into a dictionary
data = [('a', 10), ('b', 20), ('c', 30)]
data_dict = {k: v for k, v in data}
print("Converted Dictionary:", data_dict)
