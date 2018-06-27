num = 10;
print(num);
#连续赋值
a = b = c = d=1;
print(a,b,c,d);
num1,num2,num3 = 1,12.2,"今天风好大，人都被吹飞了"
print(num1,num2,num3);
str = "abcdefg";
#1；4,  左闭右开区间
print(str[1],str[1:4])
str2 = "萨瓦迪卡撒浪嘿呦阿弥陀佛"
#in和 not in 关键字，用于判断是否存在
if("萨 迪" in str2):
    print("存在")
if("萨 迪" not in str2):
    print("不存在")
#复数
com = 12-12j;
print(type(com))
#打印复数的实部
print(com.real,type(com.real))
#打印复数的虚部
print(com.imag,type(com.imag))
#格式化数据
# %s  字符串， %d   整数    %f   小数
str3 = "my name is %s and my age is %d"%("胡歌",18)
print(str3)
#   %f:默认保留6位小数   格式化数据使用时注意顺序
str4 = "my name is %s and my salary is %.2f"%("小明",20000.52311111)
print(str4);
#用户输入数据,输入的数据都是字符串类型，不能直接用来进行加减
# age = input("请输入您的年龄:")
# # 将数据转换为int类型
# age = int(age);
# age = age+1;
# print(age,type(age))
#驼峰命名法   ，见名知意    a  b  yaojin
userName = input("请输入您的姓名：");
userAge = input("请输入您的年龄：");
print("您的名字是："+userName);
userAge = int(userAge);
# print("您的年龄是："+userAge)    #int类型的数据不能直接拿来跟字符串进行拼接，可以使用逗号分隔打印
print("您的年龄是：",userAge)

