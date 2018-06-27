#元组   有序   可重复   不可修改
tup1 = ("所爱隔山海","山海不可平","所爱隔山海")
print(tup1,type(tup1))
#通过下标取值
print(tup1[0],tup1[0:2])
# tup1[0] = "所爱隔山"
# print(tup1)
# del tup1[0]#不能删除某一个元素
# print(tup1)
# del tup1  #可以删除整个元组
# print(tup1)
tup2 = ("所爱隔山海","山海皆可平","海有舟可渡","山有路可行")
tupSum = tup1+tup2;
print("组合之后的元组",tupSum)
for x in tupSum:
    print(x)