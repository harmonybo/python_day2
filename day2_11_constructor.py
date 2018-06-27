class Student():
    name = "二狗";
    age = 0;
    # def __init__(self):
    #     print("学生类开始初始化了")
    def __init__(self,name):
        self.name = name;#将传入的name值赋给属性
        print("初始化")
    def __del__(self):#不使用这个类时，会调用
        print("对象要被删除了")
    def kiss(self):
        print("don't bb ,kiss me")
    def study(self):
        print("小点声儿，吵到我写代码了")
stu = Student("张三");#实例化对象会自动调用执行类中的init方法
print(stu.name)
stu.kiss()