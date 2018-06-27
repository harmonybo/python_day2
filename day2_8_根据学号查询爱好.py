#字典 ,学生管理系统
stu = {
        "001":{
                "name":"张三",
                "hobby":"女生",
                "address":"江夏区"
                },
        "002":{
                "name":"李四",
                "hobby":"唱歌",
                "address":"江汉区"
                },
        "003":{
                "name":"王五",
                "hobby":"打球",
                "address":"洪山区"
                }
        }
#让用户输入学号
stuNum = input("请输入您的学号：");
flag = False;#标识性变量
for x in stu.keys():
    if(stuNum==x):
        flag = True;
        for y in stu[x].keys():
            if(y=="hobby"):
                print(stu[x][y])
if(flag):
    print("您查找的用户存在")
else:
    print("您查找的用户不存在")
