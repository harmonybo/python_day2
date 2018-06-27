#list  列表   有序  可重复
list1 = [1,2,3,4];
print(type(list1),list1[1],type(list1[1]),list1[1:3],type(list1[2:3]))
print(list1);
#修改下标为一的数据
list1[1] = 12;
print(list1);
#列表中可以放不同类型的数据
list2 = [1,12.12,"helloworld"]
print(list2,type(list2))
#添加数据
list2.append("good night")
print(list2)
#删除数据,根据下标进行删除
#del list2[2];
#print(list2)
list2.append("helloworld")
print(list2)
#  x 可以取到列表中的每一个元素
for x in list2:
    # print("列表中的数据",x)
    #根据元素来匹配下标，当出现多个重复元素时，返回第一个下标
    print(list2.index(x),x)
list3 = ["抽烟","喝酒","烫头"]
listSum = list2+list3;
print("将两个列表组合之后的结果",listSum)
#删除整个列表
# del listSum;
# print(listSum)
