def sayhello(name):
    print("i name is {0}".format(name))
    print("hello {0}".format(name))
    print("---------------")

if __name__ == "__main__":# 在自己的文件里面调用就是文件名main如果在别的模块里被import就是模块名
    print("**"*18)
    name = input("please input your name:")
    print(sayhello(name=name))
    print("$$"*18)