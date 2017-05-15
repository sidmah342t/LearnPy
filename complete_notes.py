import random

## https://github.com/sidmah342t/LearnPy

'''

##Type what ever you want
##https://github.com/sidmah342t/LearnPy

~\PycharmProjects [master +1 ~4 -0 !]> git --version
git version 2.11.0.windows.3

###set global config variables

~\PycharmProjects [master +1 ~4 -0 !]> git config --list
core.symlinks=false
core.autocrlf=true

user.name=sidmah342t
user.email=sidmah342t@yahoo.com

## Initialize git to track a local project on git
~\PycharmProjects\LearnPy [master +1 ~4 -0 !]> git init
Initialized empty Git repository in C:/Users/siddhartha/PycharmProjects/LearnPy/.git/
~\PycharmProjects\LearnPy [master +14 ~0 -0 !]>

~\PycharmProjects\LearnPy [master +14 ~0 -0 !]> git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        .idea/
        complete_notes.py
        demo.py
        facebookplay.py
        googleapicalls.py
        kinter.py
        namesck.py
        namesroll.py
        playwithfiles.py
        test.txt
        tictactoe.py
        tkinter1.py
        trypy.py
        tupllist.py

nothing added to commit but untracked files present (use "git add" to track)
~\PycharmProjects\LearnPy [master +14 ~0 -0 !]>

## add files to staging area
~\PycharmProjects\LearnPy [master +1 ~0 -0 | +13 ~1 -0 !]> git add -A
~\PycharmProjects\LearnPy [master +14 ~0 -0 ~]> git status
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

        new file:   .gitignore
        new file:   complete_notes.py
        new file:   demo.py
        new file:   facebookplay.py
        new file:   googleapicalls.py
        new file:   kinter.py
        new file:   namesck.py
        new file:   namesroll.py
        new file:   playwithfiles.py
        new file:   test.txt
        new file:   tictactoe.py
        new file:   tkinter1.py
        new file:   trypy.py
        new file:   tupllist.py
        
        
        
##git commit
~\PycharmProjects\LearnPy [master +14 ~0 -0 ~]> git commit -m "Tried to commit Project to Git"
[master (root-commit) 565180a] Tried to commit Project to Git
 14 files changed, 698 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 complete_notes.py
 create mode 100644 demo.py
 create mode 100644 facebookplay.py
 create mode 100644 googleapicalls.py
 create mode 100644 kinter.py
 create mode 100644 namesck.py
 create mode 100644 namesroll.py
 create mode 100644 playwithfiles.py
 create mode 100644 test.txt
 create mode 100644 tictactoe.py
 create mode 100644 tkinter1.py
 create mode 100644 trypy.py
 create mode 100644 tupllist.py
~\PycharmProjects\LearnPy [master +0 ~1 -0 !]>







'''


print(random.randint(1,6))

## list
flist=['Ápple','Banana','Peach']
print(flist*2)
flist[1]='Clementine'
print(flist)
print(flist[0:2]) ## list slicing
print(flist[0:2]) ## list slicing
print(flist[1:]) ## list slicing

## list functions
flist.append('Persimmon')
flist.append('Clementine')
print(flist)
print(flist.count('Clementine'))
flist.insert(2,'Orange')
print(flist.index('Orange'))
print(flist)
print(len(flist))

## Access individual elements of a list
print(flist[0])
print(flist[1])
print(flist[1:3])
print('Slice Jumping Lists')
print(flist[1:6:2]) ## list slicing skipping

## list comprehension
print('list comprehension')
print([x**2 for x in range(1,10,3)])


## use for loop to traverse a list
for i in flist:
    print(i)

## Boolean check
if('Orange' in flist):
    print('Yes Dude.Life is Orange')

print('Pomm' in flist)

flist.clear()
print(flist)

list2=list(range(1,20,5))
print(list2)

## for loop
for i in range(1,5):
    print(i)

## use functions
print('###########')
def add(x,y):
    return (x+y)

## try and exception

try:
    20/0
except ZeroDivisionError:
    print('Cant divide with zero')

finally:
    print('This always gets executed')

print(add(2,3))

## pass function as an argument to another function
def square(c):
    return c*c

print(square(add(9,11)))

## Dictionaries
sdict = {'Stock Name':'ÍCICI','Sector':'Bank'}
print(sdict['Sector'])
print('######Dictionaries###')
print('Sector' in sdict)
print(sdict.get('Sector'))
print(sdict.get('Becck','Sorry! Key not Found'))

## Tuples. Similar to list but immutable.List are mutable
stupl = ('Abba','Becky','Carla')
print(stupl)
print(stupl[0])



## file handling
##open, read/write,close file

file = open('test.txt','w')
file.write('This is written by Advik')
file.close()

file = open('test.txt','a')
file.write(' on Mothers day.')
file.writelines(['\nLine2 \n','Line3 \n'])
file.close()

file = open('test.txt','r+')
print(file.read())
file.close()

print('Using with clause')
with open('test.txt', 'r') as f:
    read_data = f.read()
f.closed

## use for loop to loop over a file line by line
for letter in read_data:
    print(letter)


## String formatting
date1=["12","09","2017"]
print('Date printed using string format')
print('Date Format:{0}/{1}/{2}'.format(date1[0],date1[1],date1[2]))
print('test:{x}/{y}'.format(x=100,y=300))
print(','.join(['App','Milk','Shake']))

print('Hello,There'.replace('There','Likhi'))
print('Hello,There'.startswith('Hello'))
print('Hello,There'.endswith('Likhi'))
name='Likhi'
print(name.lower())
print(name.upper())
print('nestD'.upper())

print(max(1,2,3,4,66,65))
print(min(11,2,3,4,66,65))
print(abs(-1.345))



