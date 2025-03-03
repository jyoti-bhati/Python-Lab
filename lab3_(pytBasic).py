# 1. Find common elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = set(list1).intersection(set(list2))
print("Common elements:", common_elements)

# output = Common elements: {3, 4}




# 2. Unique characters in a string
string = "programming"
unique_characters = set(string)
print("Unique characters in the string:", unique_characters)

# output = Unique characters in the string: {'g', 'i', 'r', 'm', 'a', 'p', 'o', 'n'}




# 3. Union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of sets:", union_set)

# output = Union of sets: {1, 2, 3, 4, 5}




# 4. Intersection of sets
A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
intersection_set = A.intersection(B)
print("Intersection of sets:", intersection_set)

# output = Intersection of sets: {'c', 'b'}




# 5. Difference of sets
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}
difference_set = X.difference(Y)
print("Difference of sets (X - Y):", difference_set)

# output = Difference of sets (X - Y): {1, 2}




