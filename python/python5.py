'''
#类对象
class Person:
    name='liuming'
    age=12
    def printName(self):
        print (self.name)
p=Person()   #实例对象
print(p.name)   #实列访问
print(Person.name)   #类名访问
p.printName()  #访问类方法
print("--------------")
'''

'''
#改变类属性必须使用类名
class Person:
    name='liuming'
    age=12
    def printName(self):
        print (self.name)
p1=Person()
p=Person()
p.name="lihua"
print(p.name)
print(p1.name)
print(Person.name)
print("--------------")
Person.name="sunli"
print(p.name)
print(p1.name)
print(Person.name)
'''

'''
#访问权限
class person:
    __name="json"#私有的
    __age=12
    def show():
        print(person.__age,person.__name)
    def __show1(self):#私有的
        print("__show1")
#print(person.__name,person.__age)  #在外部访问不了
print(person.show())
'''

'''
#类属性
class person:
    name="lihua"
    gender="x"
    age=12
p=person()
print(p.name,p.age,p.gender)
print(person.name,person.age,person.gender)#类属性一般通过类名称访问
p.gender="y"  #p为实例属性，为这个对象实例赋值，那么如果该对象实例存在这个属性，这个属性的值就被改变，但
              #是如果不存在该属性就会自动为该对象实例创建一个这样的属性。
p.age=24
p.name="xiaofan"
person.name="lihua1"
person.age=121
person.gender="x1"
print(p.name,p.age,p.gender)
print(person.name,person.age,person.gender)

'''

'''
#1.实例方法
class person:
    __name="jam"
    __age=12
    def getname(self):
        return self.__name
    def getage(self):
        return self.__age
    def getnum():#需要括号加self不然会报错：TypeError: getnum() takes 0 positional arguments but 1 was given
        return 2
p=person()
#print(p.getname(),p.getage())#实例方法
#print(person.getname(person),person.getage(person))
#print(person.getnum())
print(p.getnum())  #error
'''

'''
#2.类方法
class person:
    __name="jam"
    __age=12

    @classmethod #定义类方法关键字，类方法一般用类的名称来调用
    def show(cls):
        print(cls.__name,cls.__age)
person.show()
'''

'''
#3.静态方法  用类名称调用
class person:
    __name="lihua"
    __age=12

    @staticmethod
    def display():#不会传递任何参数给
        print(person.__name,person.__age)
    @classmethod
    def show(cls):#会将类名传递给cls
        print(cls.__name,cls.__age)
person.show()
person.display()
'''

'''
#编写个人信息的实例方法、类方法、静态方法
class person:
    name="lihua"
    gender="x"
    age=12
    def instanceshow(self):
        print(self.name,self.gender,self.age)
    @classmethod
    def classshow(cls):
        print(cls.name,cls.gender,cls.age)
    @staticmethod
    def staticshow():
        print(person.name,person.gender,person.age)
p=person()
p.instanceshow()#实列方法
person.instanceshow(p)#传递实列对象即可

person.classshow()#类方法

person.staticshow()#静态方法
p.staticshow()#不需要传入参数
'''

'''
#对象初始化  构造函数  析构函数
class person:
    def __init__(self,n):#初始化
        print("__init__",self,n)
        self.name=n
    def __del__(self):#析构
        print("__del__",self)
    def show(self):#实例方法
        print("show",self,self.name)

p=person("james")
p.show()
print(p)
'''

'''
#对像初始化
class person:
    def __init__(self,n,g,a):
        self.name=n
        self.gender=g
        self.age=a
    def show(self):
        print(self.name,self.gender,self.age)
p=person("james","male",21)#name  gender  age实列对像自己属性，不是类person的类属性
p.show()
person.show(p)
'''


'''
#python中构造函数只能出现一次，通过默认参数实现函数重载
class person:
    def __init__(self,n="",g="",a=0):
        self.name=n
        self.gender=g
        self.age=a
    def show(self):
        print(self.name,self.gender,self.age)

a=person("james")#error
b=person("james","female")
c=person("james","male",20)#构造属性为实例的，不是类的
a.show()
b.show()
c.show()
'''


'''
#类的实列方法至少带一个参数self,第一个参数为self
class mydata:
    __months=[0,31,28,31,30,31,30,31,31,30,31,30,31]   #私有的
    def __init__(self,y,m,d):
        if y<0:
            raise Exception("无效年份")
        if m<1 or m>12:
            raise Exception("无效月份")
        if y%400==0 or y%4==0 and y%100!=0:
            mydata.__months[2]=29
        else:
            mydata.__months[2]=28
        if d<1 or d>mydata.__months[m]:
            raise Exception("无效日期")
        self.year=y
        self.month=m
        self.day=d
    def show(self):#实列的方法
        print("%04d-%02d-%02d" %(self.year,self.month,self.day))

try:
    d=mydata(2019,12,27)
    d.show()
except Exception as e:
    print(e)
'''


#类的继承
class person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def show(self,end='\n'):#实例方法
        print(self.name,self.gender,self.age,end=end)

class student(person):
    def __init__(self,name,gender,age,major,dept):
        person.__init__(self,name,gender,age)#继承类需要显示调用基类构造函数
        self.major=major
        self.dept=dept

    def show(self):
        person.show(self," ")
        print(self.major,self.dept)

s=student("jam","male",20,"software","computer")
s.show()





