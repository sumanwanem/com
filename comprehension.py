#create nums list 1 to 6
nums = [1,2,3,4,5,6]

strings = ["intro", "to", "list", "comprehension"]

result = []

#traditional way
for i in nums:
    i = i * 2
    result.append(i)
print(result)

#list comprehension
a = [(i * 2) for i in nums]
print(a)

result2 = []

#traditional way
for j in strings:
    j = j.upper()
    result2.append(j)
print(result2)

#list comprehension
b = [(j.upper()) for j in strings]
print(b)
