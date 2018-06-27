#自定义一个学生类
class Student():
    name = "";
    age = 0;
    def kiss(self):
        print("don't bb ,kiss me")
    def study(self):
        print("小点声儿，吵到我写代码了")
def eat():
    print("(　o=^•ェ•)o　┏━┓  吃饭>>>>>>>>>>")
eat();
stu = Student();#得到学生的实例化对象
stu.study()
stu.kiss()