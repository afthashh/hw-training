# exercise 1
# a = {"a":0,"b":1,"c":2}
# print(a)

# b=a
# print(b)

# b.update({"d":4})
# print(b)
# print(a)

# from copy import deepcopy
# b = deepcopy(a)
# print(b)
# b.update({"e":5})
# print(b)
# print(a)

# exercise 2
# a = []
# for i in range(100):
#     a.append(i)
# print(a)

# a={}
# for i in range(100):
#     a.update({i:"None"})
# print(a)

a = {i:"None" for i in range(100)}
print(a)