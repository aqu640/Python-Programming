"""
# 用迴圈計算 S
S = 1*5+ 4*8+ 7*11+ 10*14+ 13*17
"""
s =0
for a in range(1,14,3):
    print("a=",a)
    b = a +4
    print("b=",b)
    s = s + a*b
    print(int(a)*int(b))
#    print('s=',s)
"""
a = 1
while a<=13:
    b = a+4   
    s = a*b
    print(a*b)
    a += 3
"""

