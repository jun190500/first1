#Tuple List
t1 = 10, 20
print (t1)
print (type(t1))

arr1 = [range(10)]
print(arr1)
print (type(arr1))


str1 = 'hello python'
str2 = str1
# str2[0] = 'y'
# a = a + b could be written as a += b
str2 += ' journey'
print(str2 is str1)

print(str1)
result = str2.split(' ')
print(result)
result_back = '***'.join(result)
print(result_back)