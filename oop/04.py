class jingling():
    def __init__(self,x=80):
        self.tizhong = 80
        self.yanse = "hei"
        self.gaodu = 185
        self.nengliang = x
        print("精灵的能量{0},身高{1},体重{2},颜色{3}".format(self.nengliang,self.gaodu,self.tizhong,self.yanse))
    def xingzou(self):
        self.nengliang -= 1
        print("行走一次能量-1",self.nengliang)

    def tiaoyue(self):
        self.nengliang -= 2
        print("跳跃一次能量-2",self.nengliang)
    def jinshi(self):
        self.nengliang += 3
        print("进食一次能量+3",self.nengliang)


jl = jingling()
jl.tiaoyue()
jl.jinshi()
jl.xingzou()
