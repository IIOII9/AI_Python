# map(function, iterable)

def square(x):
    return x ** 2;

numbers = [1, 2, 3, 4, 5];

squared = list(map(square, numbers )); # map返回一个迭代器，需要转换为list
print(squared); # [1, 4, 9, 16, 25]

# 使用lambda函数
xs = [1, 2, 3, 4];
ys = [10, 20, 30, 40, 50];
squared_lambda = list(map(lambda x, y: x + y, xs, ys));
print(squared_lambda); # [1, 4, 9, 16,