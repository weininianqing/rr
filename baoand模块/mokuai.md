# 模块
- 一个模块就是一个包含Python代码的文件，后缀名为.py，模块就是一个Python文件
- 为什么我们要用模块
    - 程序太大编写维护不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
- 如何使用模块
    - 模块直接导入
        - 假如模块名称以数字开头，需要借助importlib帮助 import importlib
            - a = importlib.import_module("数字开头的模块名")
            - 相当于将数字开头命名的模块重新命名为a
    - 语法
        
        import module_name(模块名)
        module_name.function_name(函数名)
        module_name.class_name(类名)
        - 案例01，02，p01，p02
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余的用法跟第一种相同
        - 案例 p03
        
    - from module_name import funcl_name,class_name
        - 按上述方法选择性导入
        - 使用的时候可以直接导入内容不需要前缀
        - 案例  p04
    - from module_name import * 也不需要加前缀
        - 把模块内的所有内容都导入
- if __name__ == '__main__':
    - 可以避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口
    
# 2.模块的搜索路径和存储
- 什么事模块的搜索路径：
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表
        #案例 p05.py
- 添加搜索路径
    sys.path.append(dir)
- 模块的加载顺序
    1. 上搜索内存中已经加载好的模块
    2. 搜索Python的内置模块
    3. 搜索sys.path()路径
    
    
# 包
- 包是一种组织管理代码的方式，包存放的是模块
- 用于将模块包含在一起的文件夹就是包



- 包的导入操作
    - import package name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 注意只是导入__init__.py而不是其他模块都导入
        - 使用方式：
            package_name.func_name
            package_name.class_name.func_name()
            
        - 案例 pkg01，p06.py
        
    - import package_name as 别名
        - 用法和作用和模块一模一样
        - 注意的是此种方法是默认对__init__.py内容的导入
    - import.package.module
        - 导入包里一个具体的模块
        - 使用方法
            - package_name.module_name.func_name
            - package_name.module_name.class_name().fun_name()
        - 案例 p07
        
    - import package_name.module_name as 别名
    
    
- from ...import 导入
    - form package import module,module2.....
    - 此种导入方法不执行__init__.py的内容
    - 使用方法：
        from pkg01 import p011
        stu = p011.student()
        p011.say()
        
    - from package import *
        - 导入的是__init__.py文件中的所有函数和类
        - 使用方法：
            func_name()
            class_name.func_name
            
        - 案例 p08.py 注意此种导入的具体内容
        
    - from package.module import *
        - 导入指定包模块里面的所有内容
        - 使用方法：
                func_name()
                class__name.func_name()
                
                
- 在开发环境中经常会引用其他的模块，可以再当前包中直接导入其他模块的内容
    - import 完整的包或者模块的路径        
        
- __all__的用法
    - 在使用from package import * 的时候，*可以导入的内容
    - __init__.py中如果文件为空，或者没有__all__,那么只可以吧__init__.py内容导入
    - __init__中如果设置了__all__的值，那么按照__all__指定的子包或者模块导入
    如此则不会载入__init__的内容
    - '__all__=['module','module2','package'.......]'
    - 看案例 pkg02 p09
    
# 命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用防止命名冲突
            