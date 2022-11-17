import queue
arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
print(sorted(arr))
arr.sort()
print(arr)

arr = [('Smith', 95), ('John', 78), ('Paul', 87), ('Jack', 61), ('Ryan', 97)]

res = sorted(arr, key = lambda x : x[1], reverse = True)
print(res)

#스택
stack = []
stack.append(2)
stack.append(5)
stack.append(8)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

#큐
data = queue.Queue()
print(type(data))

data.put(2)
data.put(5)
data.put(8)
print(data)

