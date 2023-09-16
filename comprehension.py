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


#traditional way
for k in nums:
    if k > 2:
        if k != 3:
            print([k])
#list comprehension
c = [(k) for k in nums if k > 2 and k != 3]
print(c)


#traditional way
for l in nums:
    if l > 1:
        for s in strings:
            print(l,s)
#list comprehension
d =[(l,s) for l in nums if l > 1 for s in strings ]
print(d)