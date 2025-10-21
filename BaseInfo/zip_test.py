names = ["Alice", "Bob", "Charlie", "David"]
ages = [25, 30, 35, 40]

# zip() function takes two or more iterables and returns a zip object.
zipped = zip(names, ages)
print("\n")
print(f"ziped type: {type(zipped)}")
print(f"ziped object: {zipped}")
print(f"ziped list: {list(zipped)}")

person = list(zipped)
print(f"\nperson type: {type(person)}")
print(f"person object: {person}")
# 此时输出为[],因为zip对象是一个迭代器，用一次就没有了

pairs = [(1, "one"), (2, "two"), (3, "three")]
numbers, words = zip(*pairs)
# 解压
print(f"\nnumbers: {numbers}, words: {words}")
