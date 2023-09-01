# intlist
# list=[1,2,3,4]
# print(list)
    # prints given integers accordingly

# multidatatype
# multi=[2,4,"Hello",3.56]
# print(multi)
    # here you can give int,char and float values

# emptylist
# empty=[]
# print(empty)
    # in empty list the list will be empty. Its expected to change or value will be added later

# nestedlist
# nested=[1,2,3[4,5,6]]
# print(nested)
    #list within a list

# INDEXING
# li=[1,2,3,4]
# print(li[3])
    #4 will be printed

# li=[1,2,3,[4,5,6]]
# print(li[3][1])
    #5 will be printed

#Negative indexing
# list=[1,2,3]
# print(list[-1])
    # 3 will be printed

# a=[1,2,3,4,5]
# b=[4,6,5,3,1]
# c=[1,2,[1,2,3]]
# d=[[1,2,],1,2,3]
# e=[1,2,3,[4,5]]
# print(a[3],b[-1],c[2][1],d[0][1],e[1])
    #printed 4,1,2,2,2

# li=[1,2,3,4]
# li[1]=9
# print(li)
    #1,9,3,4 printed

# li=[1,2,3,4,[5,6]]
# li[4][1]=8
# print(li)
    #6 changed to 8

# Append
li=[1,2,3,4]
# li.append(9)
# print(li)
    # adds an element

# Extend
# li.extend([5,6,7])
# print(li)
    #to add multiple elements

# li.insert(2,5)
# print(li)
    # for inserting elements at specific position(1st value represent position and 2nd value denotes the no. to be added)

# a=[1,2,3,4,5]
# a.append(6)
# print(a)

# b=[4,3,2]
# b.extend([5,2,1])
# print(b)

# c=[1,2]
# c.insert(1,6)
# print(c)

# d=[1,2]
# d.extend([8,2,1])
# print(d)

# e=[1,2,3,4,5]
# e.insert(3,6)
# print(e)

# f=[5,2]
# f.insert(2,3)
# print(f)

# + operator
# li=[1,2,3]
# li2=[4,5,6]
# print(li+li2)

# * operator
# li=[1,2,3]
# print(li*3)

# li=[1,2,3,4,9]
# print(len(li))
    # prints length of a list

# delete
# li=[1,2,3,4,5]
# del li[:3]
# print(li)
    # to delete upto 3rd pos(3rd excluded)

# li=[1,2,3,4,5]
# del li[0]
# print(li)
    # to delete single element

# li=[1,2,3,4,5]
# del li
# print(li)
    # removes entire list

# remove
# li=[1,2,3,4,5,3]
# li.remove(3)
# print(li)
    # it removes specific element from list(if same element exist, then 1st element will be removed)

# pop
li=[1,2,3,4,5,3]
print(li.pop(2))

# CW
# a=[1,2,3,4]
# del a[2]
# print(a)

# b=[1,4,3,5]
# del b[2:]
# print(b)

# c=[5,6,7,8]
# del c
# print(c)

# d=[2,3,4]
# d.remove(3)
# print(d)

# e=[5,4,3,2,1]
# print(e.pop(4))







