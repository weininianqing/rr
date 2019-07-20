'''

定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处的pass必须有
    pass
# 定义一个对象
xiaohuihui = Student()


# 在定义一个类用来描述听python的学生

class pythonstudent():
    name = "wangshaohui"
    age = 18
    course = "Python"
    def zuoye(self):
        print("我在做作业")
        return None
yueyue = pythonstudent()
print(yueyue.name)
print(yueyue.age)
yueyue.zuoye()

