Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
x = "welcome to samyak Institute"
len(x)
27
x.lower()
'welcome to samyak institute'
x.upper()
'WELCOME TO SAMYAK INSTITUTE'
x.capitalize()
'Welcome to samyak institute'
x.title()
'Welcome To Samyak Institute'
x
'welcome to samyak Institute'
x.replace("Samyak","UTC")
'welcome to samyak Institute'
x.replace("samyak","UTC")
'welcome to UTC Institute'
x = x.split()
x
['welcome', 'to', 'samyak', 'Institute']
" ".join(x)
'welcome to samyak Institute'
"#".join(x)
'welcome#to#samyak#Institute'
"a"*10
'aaaaaaaaaa'
x
['welcome', 'to', 'samyak', 'Institute']
x = "mayank"
x[0]
'm'
x = "mayank is learning python"
x[0]
'm'
#indexing -negative -right to Left
x[-1]
'n'
x[-2]
'o'
x[-3]
'h'
]
>>> x[-4]
't'
>>> x[0]
'm'
>>> x[1]
'a'
>>> x[2]
'y'
>>> x
'mayank is learning python'
>>> x.find("m")
0
>>> x.find("a")#first occurence
1
>>> x.rfind("a")#last a
12
>>> x.find("a",2)
3
>>> x.index("a",2)
3
>>> x.find("X")
-1
>>> #-1 means value not found
>>> x.index("X")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    x.index("X")
ValueError: substring not found
