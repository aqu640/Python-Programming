

import random
p = 0
for circle_1 in range (4):
    for circle_2 in range(circle_1+1):
        print(p, end="")        # end=' '不換行，加空格
        p = p+1
    print(" ") # 換行