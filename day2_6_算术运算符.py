# + - * /  %取余   **   //
print(4+2,12.4-4.5,4*2,4/2)
print(8/3)
print(10%5)
print(8//3)  #整除
# /  和 //区别: // 是整除，/会取到小数
print(4**3)  #  x**y  :求x的y次方
str1 = "11.2"
str1 = float(str1)#将字符串对应的数据类型转换时，整数转换为整数，小数转换为小数
print(str1,type(str1))
num = 4;
#print(num--); #在python中，没有 ++  -- 这种写法
num+=1; # num=num+1     5
num-=1;#num = num-1      4
num*=2;#num = num*2      8
#num/=2#num = num/2       4.0
#num%=2 ;#num = num%2     0.0
num**=2;#num=num**2
print(num);

list1 = [1,12,"abc"];
#self :类似于java中的this,方法参数中有self时，可以不用管他，直接传对应的参数即可
list1.append("def")
#根据下标进行添加
list1.insert(1,True)
print(list1)