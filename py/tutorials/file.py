# 4: Lists, Tuples, and Sets

list = ['A', 10, 'B', 20, 'C']
list2 = [30, 'D']
list3 = ['}', '|']

tuple = ('A', 10, 'B', 20, 'C') # tuple is a list that all its values are const

set1 = {'A', 'B', 'C', 'D', 'A'}
set2 = {'A', 'B', 'E', 'F', 'A'}

list.insert(0, '{')
list.insert(0, '|')
list.extend(list2)
list.extend(list3)

# for item in list:
#     print(item)

# for index, item in enumerate(list):
#     print(f"{index} = {item}")

# print(help(list))

# print(list[0:2])
# print(list[2:])

# print(type(list[1]), type(list[0]))
# print(dir(list))

# print(list)

# print(set1)
# print(set2)

# print(set1.intersection(set2))
# print(set2.difference(set1))

# 5:dicrDictionaries

student = {'name': 'khalil', 'age': 20, 'courses': ['Math', 'CompSci'], 'Phone':'555-5555'}

# student['name'] = 'ksohail-'
# student['phone'] = '555-5555'

del student['Phone']
student.update({'name': 'ksohail-', 'age': 21, 'phone': '555-5555'})


# print(student)
# print(student['name'])
# # print(student['Phone'])
# # print(student.get('Phone', 'Not found'))
# print(student.get('phone', 'Not found'))

# Comprehensions

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

print([n for n in nums])

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# print my_list

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print my_list

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print my_list

# Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# print my_list

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heros)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict



# If name not equal to Peter

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print i