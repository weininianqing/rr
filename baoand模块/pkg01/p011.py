# 定义一个学生类

class student():

    def __init__(self,name="noname",age=18):
        self.name = name
        self.age = age

    def sayhello(self):
        print("大家好，我叫{0}".format(self.name))
def say():

    print("我的第一个模块")

#建议所有程序的入口都以此代码为入口
if __name__ == '__main__':
    print("dajiahaohuihui")