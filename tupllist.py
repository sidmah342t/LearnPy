fruits = ['Apples','Bananas','Oranges']
#List called fruits

print(fruits)
print(fruits[0])

#String called icecream

#A list value is a mutable data type: It can have values added, removed, or changed. However, a string is immutable
icecream = 'vannila'
print(icecream[0:3])
print(icecream[-3])
fruits.append('Peaches')

print(fruits)
print(fruits[1]*3)

f1,f2,f3,f4 = fruits

print('last fruit:' + f4)

#The benefit of using a list is that your data is now in a structure, so your program is much
#more flexible in processing the data than it would be with several repetitive variables.


for i in range(0,len(fruits)):
    print(fruits[i])

#List slicing
print('List slicing')
print(fruits[1:30])
print(fruits[1:3])

print(fruits.index('Oranges'))

# Lists are mutable where as Tuples are immutable

veggies = {'Okra','Radish'}
print(veggies)

veggies.add('Carrots')
print(veggies)


#tuples

icecreams = ('vanilla','strawberry','pistachio','butter scotch','bubblegum','mango')
tuple1 = (42,)

print(icecreams)

print(type(icecreams))
print(type(veggies))
print(type(fruits))
print(type(icecream))
print(type(tuple1))

#Python uses references whenever variables must store values of mutable data types, such as lists or dictionaries.