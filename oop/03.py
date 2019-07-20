class person():
    def __init__(self):
        pass

    def __setarrt__(self, name, value):
        print("设置的属性：{0}值为：{1}".format(name, value))
        # 下面语句会导致死循环
        self.name = value


p = person()

p.age = 18