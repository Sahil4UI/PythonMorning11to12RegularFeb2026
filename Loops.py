Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #for loop
>>> for i in range(1,11)#ending-n-1:
SyntaxError: expected ':'
>>> for i in range(1,11):
...     print(i)
... 
1
2
3
4
5
6
7
8
9
10
>>> for i in range(1,11):
...     print(i,end="")
... 
12345678910
>>> for i in range(1,11):
...     print(i,end="",sep= ",")
... 
12345678910
>>> for i in range(1,11):
...     print(i,sep= ",")
... 
1
2
3
4
5
6
7
8
9
10

for i in range(1,11):
    print(i,end=",")

1,2,3,4,5,6,7,8,9,10,

for i in range(10,0):
    print(i)

for i in range(10,0,-1):
    print(i)

10
9
8
7
6
5
4
3
2
1

for i in reversed(range(1,11)):
    print(i)

10
9
8
7
6
5
4
3
2
1
x = "hello"
for i in range(len(x)):
    print(x[i])

h
e
l
l
o

for char in x:
    print(char)

h
e
l
l
o
for i in range(1,100000):
    pass

#break-quit the loop
for i in range(1,11):
    print(i)
    break

1

for i in range(1,11):
    print(i)
    if i%2==0:
        continue

1
2
3
4
5
6
7
8
9
10
for i in range(1,11):
    
    if i%2==0:
        continue
    print(i)

1
3
5
7
9
