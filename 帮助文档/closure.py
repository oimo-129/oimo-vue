# multiplier_debug.py - 闭包函数调试示例

import inspect

def create_multiplier(factor):
    """
    创建一个乘法器闭包
    参数:
        factor: 乘数因子
    返回:
        multiplier: 一个闭包函数，将输入值乘以指定的因子
    """
    print(f"[DEBUG] 创建乘法器，factor = {factor}")
    print(f"[DEBUG] create_multiplier的局部变量: {locals()}")
    
    def multiplier(x):
        print(f"[DEBUG] 调用乘法器，参数 x = {x}，使用外部factor = {factor}")
        result = x * factor
        print(f"[DEBUG] 计算结果: {x} * {factor} = {result}")
        return result
    
    print(f"[DEBUG] 内部函数定义完成，返回multiplier函数")
    print(f"[DEBUG] multiplier.__closure__ = {multiplier.__closure__}")
    if multiplier.__closure__:
        print(f"[DEBUG] 闭包中的值: {multiplier.__closure__[0].cell_contents}")
    
    return multiplier

def show_function_details(func):
    """显示函数的详细信息，包括闭包变量"""
    print(f"\n函数名称: {func.__name__}")
    print(f"函数定义: {inspect.getsource(func)}")
    print(f"闭包信息: {func.__closure__}")
    if func.__closure__:
        for i, cell in enumerate(func.__closure__):
            print(f"  闭包变量[{i}]: {cell.cell_contents}")

def main():
    """主函数，用于测试和调试闭包"""
    print("===== 创建闭包函数 =====")
    double = create_multiplier(2)  # 创建一个双倍乘法器
    triple = create_multiplier(3)  # 创建一个三倍乘法器
    
    print("\n===== 查看闭包函数详情 =====")
    show_function_details(double)
    show_function_details(triple)
    
    print("\n===== 使用闭包函数 =====")
    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")
    
    print("\n===== 多次调用同一闭包 =====")
    print(f"double(10) = {double(10)}")
    print(f"double(20) = {double(20)}")
    
    # 演示闭包是如何记住外部变量的
    print("\n===== 创建多个闭包并比较 =====")
    multipliers = [create_multiplier(i) for i in range(1, 5)]
    for i, mult in enumerate(multipliers, 1):
        print(f"multiplier({i})(10) = {mult(10)}")

if __name__ == "__main__":
    main()