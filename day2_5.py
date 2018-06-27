#python中定义方法
def eat():
    print("热干面、豆皮真好吃~~嘤嘤嘤  o(*￣▽￣*)o")
# def trip(city,sister,age):
#     print("亲爱的"+sister+"小姐姐","我想带你去浪漫的"+city)
#     print("可惜我今年只有",age,"岁，还没有成年")
def trip(city,sister,age):
    print("亲爱的%s小姐姐，我想带你去浪漫的%s,\n可惜我还未成年,只有%d岁"%(sister,city,age))
#调用方法
eat()
trip("土耳其","迪丽热巴",16)
