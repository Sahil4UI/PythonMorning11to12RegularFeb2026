Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> 
>>> #STRING
>>> x = "*"
>>> x*10
'**********'
>>> x = "hey"
>>> len(x)
3
>>> x.center(11)
'    hey    '
>>> x.center(4)
'hey '
>>> x.center(11,"*")
'****hey****'
>>> x = x.center(51,"#")
>>> x
'########################hey########################'
>>> x.lstrip()
'########################hey########################'
>>> x.lstrip("#")
'hey########################'
>>> x.rstrip("#")
'########################hey'
>>> x.strip()
'########################hey########################'
>>> x.strip("#")
'hey'
>>> x = "        x    a   v   "
x.strip()
'x    a   v'
#String is Python's immutable data type
chr(65)
'A'
ord('A')
65
x = "hey"
x.zfill(10)
'0000000hey'
#WAP to find number of vowels and consonants
x = "asdfghaabbccddeaaio"
v,c=0,0
for char in x:
    if char.isalpha():
        if char in "aeiou":
            v+=1
        else:
            c+=1

v
8
c
11

x = "1"
y = "2"
x+y
'12'


#multi line String
x = "Python is a popular, high-level, interpreted programming language known for its simple syntax, readability, and versatility. It is widely used for web development, data science, artificial intelligence, and automation, making it an ideal, beginner-friendly language for scripting and rapid application development. 
Python.org
Python.org
 +4"
 
SyntaxError: unterminated string literal (detected at line 1)
x = '''Python is a popular, high-level, interpreted programming language known for its simple syntax, readability, and versatility. It is widely used for web development, data science, artificial intelligence, and automation, making it an ideal, beginner-friendly language for scripting and rapid application development. 
Python.org
Python.org
 +4'''

#Lists in Python
#list is python's ordered and mutable data collection
x = [10,20,30,40,50]
x.append(100)
x.append(99)
#it will store value at the end
x.insert(0,-10)
x
[-10, 10, 20, 30, 40, 50, 100, 99]
x[0]=-9876
x
[-9876, 10, 20, 30, 40, 50, 100, 99]
del x[0]
x
[10, 20, 30, 40, 50, 100, 99]
x.pop()#it will remove last value
99
x
[10, 20, 30, 40, 50, 100]
x.pop(0)
10
x
[20, 30, 40, 50, 100]
x.remove(100)#remove by value
x
[20, 30, 40, 50]
sum(x)
140
min(x)
20
max(x)
50
len(x)
4
x = [4,3,2,5,6,8,54,0]
x.sort()
x
[0, 2, 3, 4, 5, 6, 8, 54]
x.sort(reverse=True)
x
[54, 8, 6, 5, 4, 3, 2, 0]
