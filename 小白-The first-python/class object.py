class body: # 肉身的功課
    def __init__(self,slumber,work,run,graduation): # 睡覺 工讀 晨跑 研究所
        self.slumber = slumber # 睡覺=6hr 給self.slumber
        self.work = work       # 工讀
        self.run = run         # 晨跑=true
        self.graduation = graduation # 研究所="線性代數" 給self

body_1 = body(6,1,True,"線性代數") # 給 body值 丟給一個命名
print(body_1.run) # 印出body_1的跑步時數