s = "hello world"
print(s)
print(len(s))
print(s.upper())
print(s.lower())
print(s.replace("hello", "Hi"))
print(s)
print("python" in s)
name = "Alice"
print(f"Hello, {name}")
print(name is None)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2)
print(numbers)
numbers.pop(2)
print(numbers)
numbers[1] = 100
print(numbers)
squares = [x**2 for x in range(1, 8)]
print(squares)

t = ("1a", "2b", "2b", "3c", "4d")
print(t.count("2b"))
print(t.index("2b"))
print(f"The tuple is {t}")
s = {"apple", "banana", "cherry"}
print(f"The set is {s}")
s.add("orange")
s.intersection_update({"apple", "banana", "orange"})

a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)
print(f"a & b ={a&b}")
print(f"a - b = {a-b}")
# 差集
print(f"a ^ b = {a^b}")
# 对称差集

person = {"name": "John", "age": 30, "name": "alice"}
print(f"person = {person}")
print(person["name"])
for key, value in person.items():
    print(f"key: {key}, value: {value}")

# 字典不允许重复键，后面的值会覆盖前面的值
