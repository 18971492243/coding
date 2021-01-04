#内存中用 Unicode 编码存储，但是存储到磁盘中时候往往采用 GBK 或者 UTF-8 等别的编码形式
'''
#字符串类型
s="hello"
print(len(s))
print(len("武汉abc"))
print(len(""))

s="a中国"
n=len(s)
for i in range (n):
    print(s[i])
'''

'''
#ord查看内存中unicode编码即ascii编码(字符在内存中的编码)，    内存中用 Unicode 编码存储
s="hai,你好"
n=len(s)
print(n)
for i in range (n):
    print(s[i],ord(s[i]))

#chr  编码转为字符
a=chr(97)
b=chr(99)
print(a,b)
'''

'''
#字符串类型比较
def compare(a,b):
    m=len(a)
    n=len(b)
    if m<n:
        k=m
    else:
        k=n

    for i in range (k):
        if a[i]>b[i]:
            return 1
        elif a[i]<b[i]:
            return -1
    if m==n:
        return 0
    elif m>n:
        return 1
    else:
        return -1

a=input("a=")
b=input("b=")
c=compare(a,b)
print(c)

#统计字符串包含大小写字母个数
s=input("enter s string:")
count=0
for i in range (len(s)):
    if s[i]>="A" and s[i]<="z":
        count=count+1
print("count=",count)

#反转字符串
def reverseA(s):
    t=""
    for i in range (len(s)-1,-1,-1):
        t=t+s[i]
    return t
print(reverseA("reverse"))

#去掉字符串左右多余的空格
def trim(s):
    t=""
    i=0
    j=len(s)-1
    while i<=j and s[i]==" ":
        i=i+1
    while i<=j and s[j]==" ":
        j=j-1
    for k in range (i,j+1):
        t=t+s[k]
    return t

s=input("enter a string:")
print(s,"length=",len(s))
t=trim(s)
print(t,"length=",len(t))


#英文字母大小写转换
c="H"
c1="g"
d=chr(ord("a")-ord("A")+ord(c))
d1=chr(ord("A")-ord("a")+ord(c1))
print(d1)
print(d)


#将一个串中所有小写字母变大写
def myToUpper(s):
    t=""
    for i in range (len(s)):
        if s[i]>="a" and s[i]<="z":
            t=t+chr(ord("A")-ord("a")+ord(s[i]))
        else:
            t=t+s[i]
    return t

def myToLower(s):
    t=""
    for i in range (len(s)):
        if s[i]>="A" and s[i]<="Z":
            t=t+chr(ord("z")-ord("Z")+ord(s[i]))
        else:
            t=t+s[i]
    return t

s=input("enter s string:")
print("myToUpper:",myToUpper(s))
print("myToLower:",myToLower(s))


#从s的start位置开始，取出长度为length的一个子串
def subString(s,start,length):
    m=len(s)
    if start>=length:
        return ""
    t=""
    i=start
    while i<m and i<start+length:
        t=t+s[i]
        i=i+1
    return t
s="abcdefghijk"
print(subString(s,2,4))
print(subString(s,2,24))

#判断一个字符串是否对称
#方案1：把反向结果和原来的字符串比较，如果一样说明对称；
#方案2：i，j左右下标逐步进行比较如果相等则对称，如果不相等则不对称
def reverse(s):
    t=""
    for i in range (len(s)-1,-1,-1):
        t=t+s[i]
    return t

def issymmetry(s):
    t=reverse(s)
    if s==t:
        return 1
    else:
        return 0

s=input("enter a string:")
if issymmetry(s)==1:
    print("对称")
else:
    print("不对称")

#方案2
def issymmetry(s):
    i=0
    j=len(s)-1

    while i<=j:
        if s[i]!=s[j]:
            return 0
        i=i+1
        j=j-1
    return 1

s=input("enter a string:")
if issymmetry(s)==1:
    print("对称")
else:
    print("不对称")

'''

'''
#字符串操作 string[start:end:step]  start默认0 end默认列尾 step默认1
s="abcdefghijk"
print("s---",s)
print("s[0:2]---",s[0:2])#string[start:end]
print("s[:2]---",s[:2])#string[:end]  start默认0,step默认1
print("s[2:]---",s[2:])#string[start:]  start为2,end默认列尾，step默认1
print("s[2,6]---",s[2:6])#string[start:end]  start为2,end为6，step默认1
print("s[:]---",s[:])#string[:]  start默认0,end默认列尾，step默认1
print("s[::2]---",s[::2])#string[::step]  start默认0,end默认列尾，step为2
print("s[0:7:2]---",s[0:7:2])#string[:end:step]  start默认0,end为7，step为2
'''

'''
s="abcdefghijk"
print(s[7::-1])#hgfedcba  step<0  索引减小的   start=7  stop=0    step=-1
print(s[7:-1:])#hij  start=7 stop=len(s)-1 step=1
print(s[-1:])#k    start=len(s)-1  stop=len(s)  step=1
print(s[:-1:])#abcdefghij   start=0  stop=len(s)-1  step=1
print(s[7:-1:-1])#    start=7   stop=len(s)-1   step=-1--->stop=0    error
print(s[8:0:-1])#ihgfedcb   start=8   stop=0   step=-1--->stop=0
print(s[5:1:-2])#fd   start=5  stop=1  step=-2--->stop=1
print(s[4:1:-2])#    start=4   stop=1  step=-2-->stop=1
print(s[7:])
print(s[7:-1])
print(s[7:-1:1])
print(s[::-2])
print(s[:])
print(s[-2:6])
print(s[-2])
print(s[-2:])
print(s[:-2])
print(s[0:-2])
'''

'''
#字符串大小写转换
s="Process finished with exit code 0"
print(s.upper())
print(s.lower())
print(s)
#字符串查找s.find(t)   不存在返回-1
i=s.find("f")
j=s.find("it")
k=s.find("S")
print(i,j,k)
#rfind(t)  反向查找，不存在返回-1
m=s.rfind("it")
n=s.rfind("W")
print(m,n)
#s.index(t)  字符串中查找子串第一次出现位置下标，如果不存在就错误
t=s.index("it")
print(t)
#r=s.index("WW")#不存在则返回error
#print(t,r)

#s.startwith(t)判断字符串是否以子串t开始，返回逻辑值(True/False)   s.endswith(t)判断字符串是否以子串t结束，返回逻辑值
q=s.startswith("Pro")
p=s.startswith("0")
print(q,p)
'''

'''
#字符串去掉空格函数lstrip()去掉左边空格,rstrip()去掉右边空格,strip()去掉左右两边空格
s1="  Process finished with exit code 0  "
print(s1)
c=s1.lstrip()
c1=s1.rstrip()
c2=s1.strip()
print(c)
print(c1)
print(c2)
'''

'''
#字符串分离函数split(sep),分割出部分组成返回值
s2="abcabcabc"
x=s2.split("ab")#注意查看运行结果
print(x)

s1="  Process finished with exit code 0 "
x1=s1.split("is")
print(x1)

x2=s1.split(" ")
print(x2)
'''

'''
#mylower(s)实现lower()  大写转小写
def mylower(s):
    t=""
    for i in range (len(s)):
        if s[i]>="A" and s[i]<="Z":
            t=t+chr(ord("a")-ord("A")+ord(s[i]))
        else:
            t=t+s[i]
    return t

s="ADFDddf"
a=s.lower()
b=mylower(s)
print(a)
print(b)


#mystrip()实现strip()
def mystrip(s):
    i=0
    j=len(s)-1
    while i<=j and s[i]==" ":
        i=i+1
    while j>=i and s[j]==" ":
        j=j-1
    return s[i:j+1]

s=" a b "
a=mystrip(s)
b=s.strip()
print(a,len(a))
print(b,len(b))


#mysplit()实现split()
def mysplit(s,sep):
    i=s.find(sep)
    t=[]
    while i>=0:
        w=s[0:i]
        t.append(w)
        s=s[i+len(sep):]
        i=s.find(sep)
    t.append(s)
    return t

s="abcababcab"
a=s.split("ab")
b=mysplit(s,"ab")
print(a)
print(b)


#字符串查找子串
def myfind(s,t):
    m=len(s)
    n=len(t)
    if m<n:
        return -1
    i=0
    while i<=m-n:
        j=0
        while j<n:
            if s[i+j]!=t[j]:
                break
            j=j+1
        if j==n:
            return i
        i = i + 1
    return -1

s="abcdabcsdesfs"
print(myfind(s,"da"),s.find("da"))
print(myfind(s,"cd"),s.find("cd"))
'''


'''
#列表类型  列表的数据项不需要具有相同的类型
list1=['1','1','physics','中国','黄河']
print(list1)
print(type(list1))
print(list1[0])
print(list1[1:4])#截取列表1~3里面的数据
list1[1]=2#列表数字更新
print(list1)
del list1[3]#删除列表元素
print(list1)

list2=['a','b']
list3=list2+list1#列表操作的联合
list4=list1+list2
print(list3)
print(list4)
'''

'''
#列表的截取  L[start:end:step]   start默认0  end默认序列尾   step默认1
L=[1,2,3,4,5,6,7,8,9]
print(L[0:2])  #[1, 2]  start 0  stop 1  step 1
print(L[:2])  #[1, 2]  start 0  stop 1   step 1
print(L[2:])  #[3, 4, 5, 6, 7, 8, 9]   start 0  stop  1  step 1
print(L[2:-1])  #[3, 4, 5, 6, 7, 8]   start 2  stop len(L)-1  step 1
print(len(L))
print(L[0:7:2])  #[1, 3, 5, 7]     start 0  stop 6  step 2
print(L[7:0:-2]) #[8, 6, 4, 2]    start 7 stop 0  step  -2--->stop  len(L)-2  注意：运行看结果  理解起来相当于8到0
print(L[8:14])  #[9]     start 8  stop 14  step
print(L[0:-2])  #[1, 2, 3, 4, 5, 6, 7]   start 0  stop len(L)-2  step 1
print(L[-2:])  #[8, 9]  start len(L)-2  stop len(L)  step 1
print(L[-2:6])   #[]  tart len(L)-2   stop 6  step 1
print(L[::-2])  #[9, 7, 5, 3, 1]   step<0索引是减小的   start->len(L)  stop=-1  注意：查看运行结果

print(L[7:-1:-1])   #[]   start 7   stop len(L)-1  step=-1   注意：查看运行结果
print(L[8:0:-1])   #[9, 8, 7, 6, 5, 4, 3, 2]   start 8  stop 0   step -1
print(L[5:1:-2])   #[6, 4]   start 5  stop 1  step -2
print(L[4:1:-2])   #[5, 3]    start 4  stop 1  step -2
'''

'''
#判断一个元素是否在列表中in 或not in
list=['a','b','c','d']
print('a' in list)
print('A' in list)
print('A' not in list)

#在末尾添加新对象
list.append(2009)
list.append('a')
print(list)

#统计某个元素在列表中出现次数
print(list.count('a'))

#在列表末尾追加另一个序列中的多个值
list1=[2019,2020]
list.extend(list1)
print(list)
list2=list+list1
print(list2)
'''

'''
#从列表中找出某个值第一个匹配项索引位置
alist=[123,'xyz','xy','zara','abc']
print(alist.index('xy'))
print(alist.index('zara'))

#将对象插入列表
alist.insert(1,2020)
alist.insert(3,'sdfs')
print(alist)

#移除列表中某个值的第一个匹配项
alist.remove(123)
print(alist)

#删除元素del
del alist[3]
print(alist)

#弹出元素
alist.pop(0)
print(alist)


#反向列表中元素
alist.reverse()
print(alist)

#对列表元素排序(排序时原素类型必须同类型的)
alist.sort()
print(alist)
'''

'''
#列表与函数  列表作为函数参数，如果在函数中改变了列表，那调用处的列表也同时改变了(实参和形参同一变量)
def fun(list, m):
    list.append(2020)
    m=1
    print(list,m)
    return list

list=[10,20,30]
m=0
list1=fun(list,m)
print(list,m)
print(list1)
'''

'''
#根据省份查找城市
provinces=['A','B','C','D']
cities=[['a1','a2','a3','a4','a5'],['b1','b2','b3','b4'],['c1','c2','c3','c4'],['d1','d2','d3']]
#print(provinces)
#print(cities)
#print(cities[0])
#print(len(cities))

found=False
p=input("please input provinces:")
for i in range (len(provinces)):
    if provinces[i]==p:
        print(provinces[i],end=":")
        for j in range (len(cities[i])):
            print(cities[i][j],end=" ")
        found=True
        break
if not found:
    print("no this provinces")


#根据城市查找省份：
def search(c):
    for i in range (len(cities)):#4
        print("i=",i)
        for x in cities[i]:#for循环列表类型
            #print(cities[i])
            #print(x)
            if x==c:
                print(c,"在",provinces[i]+"省")
                return
    print("no search")

c=input("please input city:")
search(c)
'''

'''
#元组类型   元组只能读取，不能改写
s=(1,3,2,3,4,5)
print(s)
print(type(s))

#在函数参数末尾使用*参数，元组就是可变参数，只能放到参数末尾
def fun(x,y,*args):
    print(x,y,args)
fun(1,2)
fun(1,2,3)
fun(1,2,3,4)
'''

'''
#求最大值
def max(*agrs):
    print(agrs)
    m=agrs[0]
    for i in range (len(agrs)):
        if m<agrs[i]:
            m=agrs[i]
    return m

print(max(1,2))
print(max(1,2,3))
'''

'''
#字典类型  key  --  value   键值是唯一的，值则不必
#访问字典里的值
dict={'alice':'123','beth':'13','cecil':'3258'}
print(type(dict))
print(dict['alice'])
print(dict['beth'])
print(dict['cecil'])

#修改字典
dict['alice']=1
dict['class']='2'
print(dict)

#删除字典元素
del dict['alice']#删除键是alice的条目
print(dict)
dict.clear()#清空词典所有条目
print(dict)
'''

'''
dict={'alice':'123','beth':'13','cecil':'3258'}
del dict#删除词典
print(dict)
'''

'''
#1.不许同一个键出现2次，同一个键被赋值2次，后一个值会被记住
#2.键值须不可变，可以用数字，字符串，元组充当，列表就不行
dict={1:'123','beth':'13',(1,2):'1235'}
#dict={1:'123','beth':'13',(1,2):'1235',['11']:'12'}  error
print(dict)

#字典长度
print(len(dict))
#清除字典里数据
dict.clear()
print(dict)
del dict
print(dict)  #删除字典
'''

'''
#获取字典所有键值函数
dict={1:'123','beth':'13',(1,2):'1235'}
print("keys: ",dict.keys())

#返回指定键的值
print(dict.get(1))
print(dict.get('1'))#若值不在字典中返回默认值None
print(dict.get((1,2)))#None
'''

'''
#字典存储学生信息
def getstudent():
    global  st#全局变量定义
    st=[]#列表初始化
    st.append({"name":"xiaoming","gender":"man","age":"12"})#字典插入列表
    st.append({"name":"lihua","gender":"man","age":"13"})
    st.append({"name":"xiaofan","gender":"woman","age":"22"})

def seekstudent(name):
    for s in st:#列表使用
        if s["name"]==name:
            print(s)
            print(s["name"],s["gender"],s["age"])
            return
    print("no this name")

getstudent()
seekstudent("lihua")
seekstudent("sss")
'''

'''
#字典作为函数参数
# 如果在函数中改变了字典，那么调用处的字典也同时被改变，也就是说调用处的实际参数与函数形式参数是同一个变量
def fun(dict):
    dict["name"]="xxx"
dict={"name":"xiaoyun","age":"18","six":"man"}
print(dict)
fun(dict)
print(dict)
'''

'''
#函数返回字典
def fun():
    dict={}
    dict["name"]="aaa"
    dict["age"]=12
    dict["gender"]="male"
    return dict
def show(dict):
    keys=dict.keys()
    for key in keys:
        print(key,dict[key])
dict=fun()
print(dict)
show(dict)
'''


'''
#字典与字典参数   **表示字典可变参数
# 如果函数有*args及**kargs参数同时存在时，那么*args必须放在**kargs前面，函数最后2个参数为*args,**kargs
def fun(x,y=2,**kargs):
    print(x,y)
    print(kargs)
fun(1,2)
fun(1,2,z=3)
fun(1,2,a=3,b="demo")
fun(x=1,y=2,z=3)
fun(y=1,x=2,z=5,s="demo")
fun(x=1,z=3)
'''

'''
#具有元组可变参数与字典可变参数的函数
def fun(x,y=2,*args,**kargs):
    print(x,y)
    print(args)
    print(kargs)
fun(1,2)
fun(1,2,3,4)
fun(1,2,3,4,z=5,s="demo")
#fun(x=1,y=2,3,4)   #error
#由于*args 的参数时位置参数，因此有*args 出现时，*args 前面的函数参数在调用时不能
#以关键字参数的方式出现，只能以位置参数的方式出现，例如下列是错误的调用：
#fun(x=1,y=2,3,4)
'''

'''
#字典存储省份与城市

def append(province,cities):

    if province not in provinces.keys():
        provinces[province]=cities
    else:
        print(province+"已经存在")
    print(provinces)


def show():
    for p in provinces.keys():
        print(p,provinces[p])

def seekprovince(province):
    if province in provinces.keys():
        print(province,end=":")
        for c in provinces[province]:
            print(c,end=" ")
        print()
    else:
        print("没有这个省份")

def seekcity(city):
    for p in provinces.keys():
        if city in provinces[p]:
            print(city+"属于"+p+"省")
            return
    print("没有这个城市")

provinces = {}
append("广东",["广州","深圳"])
append("四川",["成都","内江"])
append("贵州",["贵阳","六盘水"])
print(provinces)
show()
seekprovince("四川")
seekprovince("xx")
seekcity("深圳")
seekcity("xxx")
'''


























