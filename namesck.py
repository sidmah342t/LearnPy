from random import *


def roll(n, m):
    # Define a list and Collect all results into a list
    numlist = []
    for i in range(n):
           numlist += [randint(1, m)]
    return numlist


def disp_ct(lst):
    ct = 0
    for i in lst:
        ct += 1
        print('Entry No: ' + str(ct) + ' ' + nlist[ct-1] + ' ' + 'occurred' + ' ' +  str(i) + ' times')


n1 = input('key in number of times to roll:  ')
n1 = int(n1)
n2 = input('key in number of names you have got: ')
n2 = int(n2)
ct=0
nlist = []
while ct < n2:
    ct += 1
    name = input('Enter Name')
    nlist += [name]



a = roll(n1, n2)
print(a)
# print the list and pass the list to a for loop and count
tup_ct = (0,) * n2
lst_ct = [0, ] * n2
print
tup_ct
print
lst_ct
for i in a:
    lst_ct[i - 1] = lst_ct[i - 1] + 1

print
lst_ct
disp_ct(lst_ct)