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
#遍历学生的所有key
# for x in stu.keys():
#     print(x)
for x in stu.values():  # x 取得是 {"name":"张三","hobby":"女生","address":"江夏区" }
         # print(x,type(x))
    for y in x.keys():
        print(y,x[y])