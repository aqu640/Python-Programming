
"""
# 課堂1 印出下列程式
def f2(b):
    global j
    print(j)
    for j in range(b):
        print(chr(i+65),end="")
    
def f3(c):
    for j in range(c):
        cc=9-j-i
        print(cc, end="")
j=0
for i in range(10):
    f1(10-i)
    f2(i*2+1)
    f3(10-i)
    print("")

for i in range(10):
    a=10-i
    for j in range(a):
        print(j, end="")
    b=i*2+1
    for j in range(b):
        print(chr(i+65),end="")
    c=10-i
    for j in range(c):
        print(9-j-i, end="")
    print("")

"""
"""

print(" 3210A0123","\n",
       "321BBB123","\n",
       "32CCCCC23","\n",
       "3DDDDDDD3","\n",
       "32EEEEE23","\n",
       "321FFF123","\n",
       "3210G0123")
"""
def f2(b):
    global j
    print(j)
    for j in range(b):
        print(chr(i+65),end="")
    
def f3(c):
    for j in range(c):
        cc=9-j-i
        print(cc, end="")
j=0
for i in range(10):
    f1(10-i)
    f2(i*2+1)
    f3(10-i)
    print("")

for i in range(10):
    a=10-i
    for j in range(a):
        print(j, end="")
    b=i*2+1
    for j in range(b):
        print(chr(i+65),end="")
    c=10-i
    for j in range(c):
        print(9-j-i, end="")
    print("")
