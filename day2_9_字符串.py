str1 = "to be true to yourself"
print(str1.find("ie"));#find方法，当字符串中存在要查询的字符时，返回下标,不存在时，返回-1
print(str1.find("e",1,5))#坐标在1 和3之间，且左闭右开的范围内，去查询 b
strJoin = "#".join(["my","name","is","huge"]);
print(strJoin,type(strJoin))#进行多个字符之间的连接
str2 = "my*age*is*18"
strSplit = str2.split("*")#按*对字符进行切割,得到对应的字符组成的列表
print(strSplit,type(strSplit))
str3 = "hello world";
strReplace = str3.replace("l","h");#将字符 l 替换成  字符 h
print(strReplace)
str4 = "hello";
print(str4.upper());#将字符串转换成对应的大写字母输出
str5 = "HELLO";
print(str5.lower())#将字符串转换成对应的小写字母输出
