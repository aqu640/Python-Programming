"""
13. Roman to Integer

I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""

class Solution(object):
    def __init__(self, s):
        self.s = s
    def romanToInt(self, s):

        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        
        for i in range (len(s)):

            if i >0 and d[ s[i] ] > d[ s[i-1] ]:        
                result += d[ s[i] ] -2* d[ s[i-1] ]

            else:
                result += d[ s[i] ] 
        return  result



n = Solution("MCMXCIV")
print("n=", n.romanToInt("MCMXCIV"))

"""
MC = 1000+100 = 1100
CM = 1000-100 = 900
MCM = 1900 = 1000+100 -100*2
MX = 10
MCMX = 1910
XC = 100-10*2 (MCMX +XC -X )
MCMXC = 1990
CI
MCMXCI
IV




class Solution(object):
    def __init__(self, s):
        self.s = s
    def romanToInt(self, s):

        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        
        for i in range (len(s)):
            
            print("i=",i)
            if i >0 and d[ s[i] ] > d[ s[i-1] ]:
                print("s[i] _1 = ",s[i])
                print("d[ s[i] ]=",d[ s[i] ])  
                print("d[ s[i-1]]=",d[ s[i-1] ])                  
                print("result_1=",result)
                
                result += d[ s[i] ] -2* d[ s[i-1] ]
                print("result_2=",result,"\n")
            else:
                print("s[i] _2 = ",s[i])

                result += d[ s[i] ] 
                print("result_3=",result,"\n")
        return  result

"""






