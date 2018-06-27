#字典:  "name":"张三"   key:value  注意：key不能重复，value可以
#如果key出现重复，后面的key value会将之前的覆盖
dict1 = {"name":"张三","name":"李四","age":18,"address":"湖北省武汉市东西湖区","Id":20130201}
print(dict1,type(dict1))
#通过key  来取value
print(dict1["name"])
#  dict_keys   获取字典的所有key集
#(['name', 'age', 'address', 'Id'])  获得类型为存放着列表的元组
dictKeys = dict1.keys();
print(dictKeys,type(dictKeys))
#dict_values  获取字典的value集
dictvalues= dict1.values();
print(dictvalues,type(dictvalues))
#使用for循环遍历字典的key集
for x in dictKeys:
    value = dict1[x]
    print(x,value)
#获得字典的item集
dictItems = dict1.items();
print(dictItems)
for x in dictItems:
    print(x,type(x))
