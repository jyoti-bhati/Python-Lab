# Simple comparision
"""n=[3,4,5,6,7]
squares=[x**2 for x in n]
print(squares)"""


#With condition filters even numbers
"""even_nums=[x for x in range(20) if x%2==0] 
print(even_nums)"""


#nested loops
"""co_ordinates=[(x,y) for x in range(5) for y in range(3)]
print(co_ordinates)"""

#With if else condition
"""result = ['Even' if num%2==0 else 'Odd' for num in range(10)]
print(result)"""

#Create a list of numbers between 1 and 50 that are divisible by 5.
"""num=[x for x in range(1,51) if x%5==0]
print(num)"""


#Given a string: "comprehension", create a list of all the vowels in the string.
"""input_string = "comprehension"
vowels = "aeiou"
vowel_list = [char for char in input_string if char in vowels]
print(vowel_list)"""


#Write a list comprehension to generate all prime numbers less than 50.
"""num=[n for n in range(2,50) if all(n%i!=0 for i in range(2,int(n**0.5)+1))]
print(num)"""



#Create a list of their factorials using list comprehension.
input_set = {1, 2, 3, 4, 5}
for item in input_set:
    fact = 1
    for number in range(1,item+1):
        fact = fact * number
        print ("Factorial of", input, "is", fact)




