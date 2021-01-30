#yield 生成器

def test_provider():
    # 循环读取数据
    for i in range(10):
        print("开始操作")
        yield i
        print("结束操作")

p = test_provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))