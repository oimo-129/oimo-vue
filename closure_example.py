# Python闭包示例文件

def create_counter(start=0):
    """
    创建一个计数器闭包
    参数:
        start: 计数器的初始值，默认为0
    返回:
        counter: 一个闭包函数，每次调用会使计数器加1并返回当前值
    """
    # start是自由变量，它被内部函数引用
    def counter():
        # 使用nonlocal关键字声明start不是局部变量
        nonlocal start
        start += 1
        return start
    
    # 返回内部函数，形成闭包
    return counter


def create_multiplier(factor):
    """
    创建一个乘法器闭包
    参数:
        factor: 乘数因子
    返回:
        multiplier: 一个闭包函数，将输入值乘以指定的因子
    """
    def multiplier(x):
        return x * factor
    
    return multiplier


def create_power_function(exponent):
    """
    创建一个幂函数闭包
    参数:
        exponent: 指数
    返回:
        power: 一个闭包函数，计算输入值的幂
    """
    def power(base):
        return base ** exponent
    
    return power


# 演示闭包的使用
if __name__ == "__main__":
    # 示例1：计数器闭包
    print("=== 计数器闭包示例 ===")
    counter1 = create_counter()  # 创建一个计数器，初始值为0
    print(counter1())  # 输出: 1
    print(counter1())  # 输出: 2
    
    counter2 = create_counter(10)  # 创建另一个计数器，初始值为10
    print(counter2())  # 输出: 11
    print(counter2())  # 输出: 12
    print(counter1())  # 输出: 3 (counter1和counter2是独立的闭包)
    
    # 示例2：乘法器闭包
    print("\n=== 乘法器闭包示例 ===")
    double = create_multiplier(2)  # 创建一个双倍乘法器
    triple = create_multiplier(3)  # 创建一个三倍乘法器
    
    print(double(5))  # 输出: 10
    print(triple(5))  # 输出: 15
    
    # 示例3：幂函数闭包
    print("\n=== 幂函数闭包示例 ===")
    square = create_power_function(2)  # 创建一个平方函数
    cube = create_power_function(3)    # 创建一个立方函数
    
    print(square(4))  # 输出: 16
    print(cube(4))    # 输出: 64 