'''人工智能程序设计'''

# print(dir(__builtins__))
# help()

# def hanglieshi(a,b,c,d,e,f,g,h,i):
#     print(a*e*i+b*f*g+c*d*h-c*e*g-d*b*i-a*h*f)
# hanglieshi(11,12,13,21,22,23,31,32,31)


import random
import string

"""
第一章：
"""
# import test
# test.main()


"""
第二章：运算符，内置函数
"""
# 不支持++和--,++表示为两个正号，--得正
# a=2
# a+=1;print(a)
# a-=1;print(a)
# a*=2;print(a)
# a/=2;print(a)

# a=2
# # a=2,即0010,9=1001
# # a|=9表示0010 OR 1001 = 1011,结果a=11
# a|=9;print(a);
# # a=2,即0010,9=1001,1001 AND 0010 = 0000
# a&=9;print(a)

# a**=3;print(a)
# a//=3;print(a)

'''类型判断与转换'''
# bin()2进制,oct()8进制,hex()16进制
# print(bin(2),oct(2),hex(2))

# 'inf'表示无穷大
# print(float('inf')>0.1)
# a=complex(3,2)
# print(a)


# print(ord('a'),ord('b'),ord('y'))
# print(chr(47),chr(58),chr(65))
# print(chr(ord('A')+1),chr(ord('学')+1))

# print(dict(zip('1234','abcd')))
# print(set('hafajdsfkj'))

# print(eval('23'))
# print(eval(str({'a':1,'b':2})),eval(str((2,3,6,7))))

# a=(i for i in range(5))
# print(isinstance(3,int),isinstance('3',str),isinstance(a,type(a)))


# max,min,sum
# # max支持key
# a=[[random.randint(1,100) for i in range(5)] for i in range(10)]
# print(a)
# print(max(a,key=lambda i:i[1]))
# b=[[1,4,1,5,1],[1,4,1,7,1],[1,1,1,1,1,1],[2,1,1,1,1]]
# print(max(b,key=lambda s:(s[1],s[3])));'''当第2个元素相等时，比较第4个'''

# print(1,2,3,4,5,sep='aa',end='.')

'''sorted排序'''
# a=list(range(1,11));print(a)
# random.shuffle(a);print(a)
# a=sorted(a);print(a)

# a=[[random.randint(1,10) for i in range(5)] for i in range(10)]
# print(a);'''重复'''

# b=[random.sample(range(10),5) for i in range(10)]
# print(b);'''不重复'''
# b=sorted(b);print(b)
# b=sorted(b,key=lambda x:(x[2],x[0],x[1]))
# print(b)

# a=list(range(10,0,-1))
# a=sorted(a,reverse=False)
# print(a)

# a=[['aaa','b','cc'],['gggg','g','gg'],['ppppp','p','pppp']]
# a=sorted(a,key=lambda x:(x[1],x[2],x[0]),reverse=True)
# print(a)

'''enumerate'''
# a='abcd'
# print(tuple(enumerate(a)))

# for x,y in enumerate(range(10,15)):
#     print((x,y),end=' ')


# word=string.digits+string.ascii_lowercase
# b=' '.join((random.choice(word)) for i in range(10))
# print(b)


'''map(函数,所映射序列)'''
# a=list(map(int,'59659'))
# print(a)

# def ower(a):
#     return ''.join(i.lower() for i in a)

# def lower(A):
#     a=''
#     for i in A:
#         achar=i.lower()
#         a+=achar
#     return a

# def lower(A,B):
#     a=''
#     for i in A:
#         achar=i.lower()
#         a+=achar
#     b = ''
#     for i in B:
#         achar = i.lower()
#         b += achar
#     return a,b
#
# # print(tuple(map(lower,'ASDFG')))
# print(dict(map(lower,"KUNMING","SHENZHEN")))
# print(dict(zip("SHENZHEN","KUNMING>")))

'''reduce'''
from functools import reduce
# def addl(a,b):
#     return a+b
# print(reduce(addl,range(1,11)))

# print(reduce(lambda x,y:x+y,range(1,11)))

'''filter'''
# 单参数函数，返回序列中使函数return为True的元素

# a=['3' in '32',3<2,'o'!='0',True]
# print(list(filter(lambda x:x,a)))

# def func(x):
#     return str.isalnum()
# print(list(filter(func,'hFeJYTlYJlKKSowJToJrlWWd')))
#
#
# def str_list(a):
#     list1=[]
#     for i in a:
#         list1.append(i)
#     return list1
# a=str_list('hFeJYTlYJlKKSowJToJrlWWd')
# print(list(filter(str.islower,a)))
# 这里islower后加括号会报错的原因是加了括号就会作为函数立即调用，而不加就会作为一种方法被filter使用

# str.isalpha()：检查字符串是否只包含字母。
# str.isdigit()：检查字符串是否只包含数字。
# str.isalnum()：检查字符串是否只包含字母和数字。
# str.isspace()：检查字符串是否只包含空白字符。
# str.istitle()：检查字符串是否是标题化的（即每个单词的首字母大写）。
# str.islower()：检查字符串是否全部小写。
# str.isupper()：检查字符串是否全部大写

'''zip'''
# print(list(zip('abcd')))
# print(list(zip(range(1,5),'abcd')))
# print(list(zip(range(1,7),'昆明理工大学','广东工业大学')))

# for i in zip(range(3),'abc'):
#     print(i);'''zip可迭代'''

# a=zip(range(3),'xyz')
# print(list(a))
# print(list(a))
# # 这里的a表示由zip生成的迭代器，在第一次转化为列表被print后，就被“消费”了
#
# a=list(zip(range(3),'xyz'))
# print(a)
# print(a)
# # 这里的a表示由迭代器转化的列表，在赋值市已经转化为列表，故a为列表，可以遍历多次
# #总结：迭代器能从前往后遍历，但是只能遍历一次，之后销毁



"""
第三章：Python序列结构
"""


'''列表'''

'''创建列表'''
# print(list((1,2,3)))
# print(list(range(1,4)))
# print(list('hello world'))
# print(list({1,2,3}))
# print(list({'a':1,'b':2,'c':3}))'''把字典的键转化为列表'''
# print(list({'a':1,'b':2,'c':3}.items()));'''把字典元素转化为列表'''

'''删除列表'''
# x=[1,2,3]
# del x
# print(x)

'''访问列表元素'''
# list=[1,2,3,4,5]
# print(list[0],list[1],list[-1],list[-2],list[0:3],list[0:],list[:-1],list[:])
# '''切片为空默认为0'''

'''列表函数'''
'''x.append()'''
# x=[1,2,3]
# x.append(4),print(x)

'''x.insert()'''
# x.insert(2,2.5),print(x)
# x1 = [5,6,7]

'''x.extend()在末尾插入列表'''
# x.extend(x1),print(x)

'''x.pop()'''
# x=[1,2,3]
# x.pop(2),print(x)

'''x.remove(),del x[a]'''
# x.append(1),print(x)
# x.remove(1),print(x)
# del x[-1];print(x)
# x.insert(0,1),print(x)

'''count统计某元素出现个数,index返回该元素第一次出现的位置'''
# x=[1,2,2,2,3]
# print(x.count(2))
# print(x.index(2))
# print(x.index(4));'''抛出异常'''

'''sort,reverse'''
# import random
# x=list(range(1,11))
# random.shuffle(x),print(x)
# x.sort(key=lambda x:x,reverse=False)
# print(x)
# x.sort(key=lambda x:-x,reverse=False),print(x)
# x.sort(key=lambda x:x,reverse=True),print(x)

'''+,*,in,>,=='''
# x=[1,2,3];x=x+[4];print(x)
# x=x*2;print(x)
# bool1 = 3 in x;bool2=7 in x;print(bool1,bool2)
# y=[1,2,2,4];print(x>y)

'''sum'''
# a=[1,2,3,4]
# b=sum(a)
# print(b)


'''all,any,max,min,sum,len,zip,enumerate'''
# all(x)查看x中元素是否都为True,即非0
# any(x)查看x中是否存在等价于True的元素
# max(x,key=str)将x中元素转化为字符串后比较最大
# zip(x,y)组合列表x,y中各个元素
# import random
# x=list(range(1,11))
# y=list(range(1,11))
# random.shuffle(x),print(x)
# random.shuffle(y),print(x)
# x.sort(key=lambda x:x,reverse=False);print(x)
# print(all(x),any(x),max(x),max(x,key=str),min(x),sum(x),len(x))
# print(list(zip(x,y)))
# print(tuple(enumerate(x)))
# print(list(enumerate(x)))
# print(dict(enumerate(x)))

'''列表推导式'''
# a=[x+x for x in range(30)];print(a)
# b=[];
# for x in range(30):
#     b.append(x+x)
# print(b)

# a="昆昆昆明理工大学昆昆"
# b=a.strip("昆")
# print(b)

'''1.嵌套列表的平铺'''
# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2=[elem for Elem1 in list1 for elem in Elem1]
# print(list2)

'''2.双层循环'''
# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2 = []
# for elem1 in list1:
#     for elem2 in elem1:
#         list2.append(elem2)
# print(list2)

'''if列表推导式'''
# list1 = list(range(1,11))
# list2 = [x for x in list1 if x%3==0]
# print(list2)

# a='昆明'
# print(a.endswith('明'));'''endwith测试字符串是否以指定字符串结束'''
# import os
# print(os.listdir(('.')));'''listdir()列出当前文件夹下所有源文件,'.'表示当前文件夹'''
# print([filename
#  for filename in os.listdir(('.'))
#  if filename.endswith(('.py','.pyw'))])

'''查找列表元素最大值的每个位置'''
# a=[5,1,2,5,5,4,5]
# n=max(a)
# b=[x for x,y in enumerate(a) if y==n]
# print(b)

'''enumerate'''
# c=enumerate([[1,2,3],[4,5,6],[7,8,9]])
# print(list(c))
# print(tuple(c))
# print(list(c))

'''列表推导式中同时遍历多个可迭代对象'''
# print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
# print([(x,y) for x in [3,1,4,1,5] if x!=1 for y in [5,3,5,8] if y==5])
# a=[3,1,4,1,5];b=[5,3,5,8]
# c=[]
# for x in a:
#     if x !=1:
#         for y in b:
#             if y==5:
#                 c.append((x,y))
# print(c)

'''切片'''
'''[start:ned:step],[0:-1:1]'''

'''获取'''
# a=list(range(3,18,2))
# print(a[::],a[::-1],a[::2])
# print(a[3:6],a[0:100])


'''增加'''
'''a[len(a):]=[x]在列表最后增加元素x,a[4:]=[x]将列表4号元素后替换为一个x'''
# a=[3,5,7];print(len(a))
# a[len(a):]=[9];print(a)
# a[2:]=[0];print(a)
# a[:0]=[1,2];'''在列表头部插入元素1,2'''
# a[3:3]=[4];'''在列表中间插入元素'''
# print(a)

'''替换和修改'''
# a=list(range(1,11))
# a[3:6]=[6,5,4];print(a);'''a[b:c]=[...]把列表从b到c-1的元素替换'''
# a[1::2]=list(range(10,1,-2));print(a);'''隔一位改一个'''

'''删除'''
# a=list(range(1,11))
# a[2:4]=[];print(a);'''3-5的三个元素变为空'''


'''元组'''

'''创建与访问'''
# a=(1,);b=(1)
# print(type(a),type(b))
# a=tuple(range(1,11));print(a[1:5])
# '''元组不可变，索引可用'''

'''生成器表达式,只能访问一次'''

# b=(i**2 for i in range(1,11))
# print(type(b));'''生成器表达式'''
# print(tuple(b));'''以元组形式打印'''
# print(list(b));'''生成器对象已经遍历结束'''

'''b.__next__(),next(b)'''
# b=(i**2 for i in range(1,11))
# print(b.__next__(),b.__next__(),next(b))
# b=(i**2 for i in range(1,11))
# for i in b:
#     print(i,end=" ")
# print()

'''map,zip,enumerate,filter等都一样'''
# b=map(str,range(5))
# print('2' in b,'2' in b,'8' in b)
# '''第一次遍历有，第二次遍历无'''


'''字典'''
# dict1={'a':1,'b':2,'c':3};'''赋值'''
# dict2=dict(a=1,b=2,c=3);'''关键参数'''
# list=[1,2,3];list2=['a','b','c']
# dict3=dict(zip(list,list2))'''zip整合'''
# print(dict1,dict2,dict3)
# dict1=('a','b','c');dict2=(1,2,3)
# dict4=dict.fromkeys(dict1,dict2)
# print(dict4)
# del dict4

'''字典元素访问'''
# dict1={'a':1,'b':2,'c':3}
# print(dict1['a']);'''dict['a']'''
# print(dict1.get('b'),dict1.get('i'))
# print(dict1.get('b'),dict1.get('i','o'))
'''dict.get('a')'''
# 如果get括号中只有键，而对象无该键，则返回空
# 但如果get括号中有键和值，而对象无该键，则返回该值

# for i in dict1:
#     print(dict1[i],end=" ") ;'''默认遍历键'''
# print()

# for i in dict1.items():
#     print(i,end=" ");'''指定遍历元素'''
# print()

# for i in dict1.values():
#     print(i,end=" ");'''指定遍历值'''

# print(dict1.items())
# print(dict1.keys())
# print(dict1.values())

'''元素的增删改'''
# 以赋值运算符操作，存在则改变值，不存在则创建新键值对
# dict1={'age':18,'name':'dog','sex':'male'}
# dict1['age']=20;print(dict1)
# dict1['score']=100;print(dict1)

# dict.update({})更新或者添加元素
# dict1={'age':37,'score':[98,97],'name':'dog','sex':'male'}
# dict1.update({'a':97,'age':39})
# print(dict1)

# popitem默认弹出最后一个元素,pop弹出指定键对应的值
# dict1={'age':37,'score':[98,97],'name':'dog','sex':'male'}
# print(dict1.popitem())
# print(dict1)
# print(dict1.pop('score'))
# print(dict1)


# 统计由1000个字符构成字符串中各字符的出现次数


# x='abcdefg'
# a=''.join((random.choice(x) for i in range(10)))
# print(a)

# a=string.ascii_letters+string.digits
# exp=''.join((random.choice(a) for i in range(1000) ))
# d=dict()
# # d.get(i,0)表示获取键为i的值，如果为空则返回0
# # 每次遍历某个字符时，就将其值加1，最后该键的值就是其出现次数
# for i in exp:
#     d[i]=d.get(i,0)+1
# # d.items()返回一个包含所有字典键值对的列表，其中每个元素是一个由键值对构成的元组
# # sorted(d.items())默认按照字符顺序排序
# for k,v in sorted(d.items()):
#     print(k,':',v)


'''集合'''
# 元素唯一且不可变
# 可以是整形，字符，元组
# 不能是列表，字典，集合（集合的元素不能是集合）

# a={3,5}
# b=set(range(1,6));print(b)
# c=set([1,1,1,2,2,3,3,3,3,])
# print(c);'''集合自动略去重复元素'''

'''元素增加与删除'''
# add增加元素，已有则忽略
# update合并两个集合，自动删除重复元素
# s={1,2,3}
# s.add(4);print(s)
# s.add(3);print(s)
# s.update({3,4,5,6})
# print(s)

# pop随机删除一个元素
# remove删除指定元素，不存在则抛出异常
# discard删除指定元素，不存在自动忽略
# s={1,2,3,4}
# s.pop();print(s)
# s.remove(4);print(s)
# # s.remove(5);print(s)
# s.discard(3);print(s)
# s.discard('e');print(s)

'''集合运算'''
# 支持len,max,enumerate等函数
# |并集  &交集  -差集  ^对称差集
# set1={1,2,3,4,5}
# set2={4,5,6,7,8}
# print(set1|set2)
# print(set1&set2)
# print(set1-set2)
# print(set1^set2)

# 生成100个由10000以内随机数组成的列表
# listrandom=[random.choice(range(10000)) for i in range(100)]
# print(set(listrandom))

# 生成给定范围的随机数
# print(random.randint(1,5))

# 生成指定范围内的一定数量的数字
# def randomnumber(number,start,end):
#     data=set()
#     while len(data)<number:
#         s = random.randint(start, end)
#         data.add(s)
#     return data
# c=randomnumber(10,1,100)
# print(c)

# 作用同上
# list=list(range(1000))
# c=random.sample(list,20)
# print(c)


'''序列解包'''

# a,b,c=1,2,3
# print(a,b,c)

# v_tuple=(False,3,'d')
# a,b,c=v_tuple
# print(a,b,c)

# x=1;y=2;print(x,y)
# x,y=y,x;print(x,y)

# x,y,z=range(3)
# print(x,y,z)

# x,y,z=map(str,range(3))
# print(x,y,z);print(type(x),type(y),type(z))


# n=int(input())
# m=range(1,n*5)
# a=random.sample(m,20)
# print(a)
# def oushu(a):
#     b=[]
#     for i in range(len(a)):
#         if a[i]%2==0:
#             b.append(a[i])
#     return b
#     # b=[i for i in a if i%2!=0]
#     # return b
# b=oushu(a)
# print(b)

# way:1
# a=random.sample(range(100),20)
# print(a)
# al=[]
# for i in range(10):
#     al.append(a[i])
# print(al)
# ar=[]
# for i in range(10,20):
#     ar.append(a[i])
# print(ar)
# all=sorted(al)
# arr=sorted(ar,reverse=True)
# result=[]
# for i in range(10):
#     result.append(all[i])
# for i in range(10):
#     result.append(arr[i])
# print(result)

# way:2
# a = random.sample(range(100), 20)
# print(a)
#
# al = sorted(a[:10])
# ar = sorted(a[10:], reverse=True)
# result = al + ar
# print(result)

# 生成随机数列表并翻转
# a=[random.randint(1,100) for i in range(10)]
# print(a)
# print(a[-1::-1])

# 阿基米德
# a=[2**(i) for i in range(64)]
# print(sum(a))
# c=sum(a)
# b=2**64-1
# print(b==c)


"""
第四章：选择与循环
"""

# if () or {} or []:
#     print(1)

# if [1,2,3] and ('a','b','c') and {':':4,';':5,'|':6}:
#     print('all right')

# i=s=0
# while s<=10:
#     i+=s
#     s+=1
# print(i)

# j=0
# for i in range(11):
#     j+=i
# print(j)

# i=s=0
# while 1:
#    i+=s
#    s+=1
#    if s>10:
#        break
# print(i)

# print(1<2<3,1>2<3,1>2>3)

'''单分支循环'''
# try:
#     x = input("Please input two numbers:")
#     a, b = map(int, x.split())
#     if a > b:
#         a, b = b, a
#     print(a, b)
# except:
#     print('damn it!waht have you done')

'''双分支循环'''
'''鸡兔同笼'''
# all,tull=map(int,input("Please input all,tull").split());'''all=总动物数,tull=总腿数'''
# # x=2*all-tull/2
# y=(tull-all*2)/2
# if int(y)==y:
#     print('鸡', int(all-y), ';兔', y)
# else:
#     print('damn it')

# jitu,tui=map(int,input().split())
# tu = (tui - jitu*2)/2
# if int(tu) == tu:
#     print('鸡：{0}，兔：{1}'.format(int(jitu-tu),int(tu)))
# else:
#     print('gg')

'''三元运算符'''
# print('3>5' if 3>5 else '3 is not larger than 5')

'''多分支'''
'''bim'''
# try:
#     tall, weight = map(float, input().split())
#     bim = weight / (tall ** 2)
#     if bim < 18.5:
#         print("过轻")
#     elif 18.5 <= bim <= 24.9:
#         print("正常")
#     elif 25 <= bim <= 29.9:
#         print("超重")
#     else:
#         print("肥胖")
# except:
#     print("数据错误")

'''score'''
# try:
#     score = int(input('Please input you score: '))
#     if score > 100 or score < 0:
#         print('data must between [0,100]')
#     elif score >= 90:
#         print('A')
#     elif score >= 80:
#         print('B')
#     elif score >= 70:
#         print('C')
#     elif score >= 60:
#         print('D')
#     else:
#         print('F')
# except:
#     print("data wrong")

'''嵌套'''
# tall, weight = map(float, input().split())
# if tall==int(tall) and weight==int(weight):
#     bim = weight / (tall ** 2)
#     if bim < 18.5:
#         print("过轻")
#     elif 18.5 <= bim <= 24.9:
#         print("正常")
#     elif 25 <= bim <= 29.9:
#         print("超重")
#     else:
#         print("肥胖")
# else:
#     print("data wrong");'''当输入为小数时'''

'''循环'''
'''1-100中能被7整除但不能被5整除的数'''
# for i in range(1,101):
#     if i%7==0 and i%5!=0:
#         print(i)

'''九九乘法表'''
# for i in range(1,11):
#     for j in range(1,i+1):
#         print('{0}*{1}={2}'.format(i,j,i*j),end=" ")
#     print()

# for i in range(2,100):
#     for x in (2,int(i)):
#         if i%int(x)==0:
#             break
#     print(i)

'''素数'''
'''for else循环:如果遍历所有均未满足条件,则跳入else'''
# low=int(input("请输入最小值："))
# upper=int(input("请输入最大值："))
# for i in range(low,upper+1):
#     for h in range(low,i):
#         if i%h==0:
#             break
#     else:
#         print(i,end=" ");'''当从2到i遍历所有h都没有能整除i,则转入else'''

# for i in range(2,10):
#     for h in range(2,i+1):
#         if i < 9:
#             print("not ok")
#     else:
#         print("You are right")

# 计算100以内最大素数
# for i in range(99,1,-1):
#     for h in range(2,i):
#         if i%h==0:
#             break
#     else:
#         print(i)
#         break

'''输入成绩'''
# list=[]
# for i in range(10):
#     print('是否输入成绩？')
#     test=str(input())
#     if test=='yes':
#         print('请输入第{0}个成绩'.format(int(i+1)))
#         score=int(input())
#         list.append(score)
#     else:
#         break
# num=sum(list)
# print('平均分是：',num/(i+1))

# L=[]
# while True:
#     qst=input('请输入成绩')
#     try:
#         L.append(float(qst))
#     except:
#         print('请输入正确的成绩')
#     while True:
#         test=input('是否要继续输入成绩:(yes/no)').lower()
#         if test not in {'yes','no'}:
#             print('请输入yes or no')
#         else:
#             break
#     if test=='no':
#         break
# print(int(sum(L))/int(len(L)))


'''时间'''
import time

# date = time.localtime()                         #获取当前日期时间
# year, month, day = date[:3]
# day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if year%400==0 or (year%4==0 and year%100!=0):   #判断是否为闰年
#     day_month[1] = 29
# if month==1:
#     print(day)
# else:
#     print(sum(day_month[:month-1])+day)


# from datetime import datetime
# def day_of_year():
#     # 获取当前日期
#     today = datetime.today()
#     # 获取今天是今年的第几天
#     day_num = today.timetuple().tm_yday
#     return day_num
# # 调用函数并打印结果
# print(f"今天是今年的第{day_of_year()}天")


'''菱形'''
# print(' '*3,'*',' '*5,'*',sep='')
# n=int(input())
# for i in range(1,n+1):
#     print(' '*(n-i),end="")
#     print(' *'*i)
# for i in range(1,n):
#     print(' '*i,end="")
#     print(' *'*(n-i))

# def main(n):
#     for i in range(n):
#         print((' *'*i).center(n*3))
#     for i in range(n, 0, -1):
#         print((' *'*i).center(n*3))
# main(4)

'''判断素数'''
# while True:
#     try:
#         n = int(input())
#     except:
#         print("请输入正确的数字")
#     for i in range(2, n):
#         if n % i == 0:
#             print("{0}不是素数".format(int(n)))
#             break
#     else:
#         print("{0}是素数".format(int(n)))
#     while True:
#         m=input("要继续测试吗?(yes/no)").lower()
#         if m not in {'yes','no'}:
#             print("请输入yes/no")
#         else:
#             break
#     if m=='no':
#         break

'''组合'''
# def intinput(n):#判断整型
#     try:
#         int(n)# 转换成功，返回True
#         return True
#     except ValueError:# 转换失败，返回False
#         return False

# def jiecheng(n):#阶乘
#     if intinput(n):
#         n=int(n)
#         if n == 1:
#             return 1
#         else:
#             return n * jiecheng(n - 1)
#     else:
#         return '错误'
# print(jiecheng('o'))

# n='8'
# print(intinput(n))  # 输出：True
# print(n)

# def zuhe(m,n):
#     return jiecheng(m)/(jiecheng(n)*jiecheng(m-n))
#
# print(zuhe(8,3))

# def Cni(n, i):
#     if not (isinstance(n,int) and isinstance(i,int) and n>=i):
#         print('n and i must be integers and n must be larger than or equal to i.')
#         return
#     result = 1
#     Min, Max = sorted((i,n-i))
#     for i in range(n,0,-1):
#         if i>Max:
#             result *= i
#         elif i<=Min:
#             result //= i
#     return result
#
# print(Cni(8,3))

'''平方和'''
# def addpingfang(n):
#     t = 0
#     for i in range(n):
#         t*=(i+1)
#     return t
#
# print(addpingfang(3))

'''阶乘和'''
# 2+6+24
# def addjiecheng(n):
#     n = int(input('请输入一个自然数：'))
#     result, t = 1, 1
#     for i in range(2, n + 1):
#         t *= i
#         result += t
#     return result
# print(addjiecheng(4))

'''去除最高最低求平均'''
# def iii():
#     score = []
#     try:
#         n = int(input("请输入评委数:"))
#         if n>=3:
#                 try:
#                     for i in range(n):
#                         m = int(input("第{0}个分数是:".format(i + 1)))
#                         score.append(m)
#                     avaiScore = (sum(score) - max(score) - min(score)) / (n - 2)
#                     return avaiScore
#                 except:
#                     print("请给出正确的分数")
#     except:
#         print("评委数至少要大于2")

# def iii():
#     score = []
#     try:
#         n = int(input("请输入评委数:"))
#         if n >= 3:
#             try:
#                 for i in range(n):
#                     # 修改了这里的字符串格式化，确保 i+1 被正确格式化
#                     m = int(input("第{}个分数是:".format(i + 1)))
#                     score.append(m)
#                     # 检查是否至少有三个分数，以避免除以零的错误
#                 if len(score) >= 3:
#                     avaiScore = (sum(score) - max(score) - min(score)) / (n - 2)
#                     return avaiScore
#                 else:
#                     print("分数数量不足，无法计算平均分")
#                     return None  # 或者可以抛出异常
#             except ValueError:
#                 print("请给出正确的分数（整数）")
#     except ValueError:
#         print("评委数必须是大于或等于3的整数")

    # 调用函数

# print(iii())

'''尼姆游戏'''
# while True:
#     try:
#         n=int(input("请输入物品总数:"))
#         if n%2!=0:
#             print("请输入偶数")
#             break
#         while True:
#             try:
#                 player = int(input("玩家决定拿走个数为:"))
#                 if player<1:
#                     print("请至少拿走一个")
#                 elif player>int(n/2):
#                     print("请最多只拿一半")
#                 else:
#                     n-=player
#                     computer=random.choice(range(1,int(n/2)+1))
#                     n-=computer
#                     print("电脑拿走个数为:",computer)
#                     print("现在n是",n)
#                 if n==2:
#                     print("玩家获胜")
#                     break
#                 if n==1:
#                     print("电脑获胜")
#                     break
#             except:
#                 print("请输入自然数")
#         if n == 2:
#             break
#         if n==1:
#             break
#
#     except:
#         print("请输入自然数")


from random import  randint
# n = int(input('请输入一个正整数：'))
# while n > 1:
#     #人类玩家先走
#     print("该你拿了，现在剩余物品数量为：{0}".format(n))
#     #确保人类玩家输入合法整数值
#     while True:
#         try:
#             num = int(input('输入你要拿走的物品数量：'))
#             #确保拿走的物品数量不超过一半
#             assert 1 <= num <= n//2
#             break
#         except:
#             print('最少必须拿走1个，最多可以拿走{0}个。'.format(n//2))
#     n -= num
#     if n == 1:
#         print('恭喜,你赢了！')
#         break
#     #计算机玩家随机拿走一些，randint()用来生成指定范围内的一个随机数
#     n -= randint(1, n//2)
# else:
#     print('哈哈，你输了。')


'''检查小于n的所有素数'''
# def qsk1():
#     qskk=[]
#     while True:
#         try:
#             n = int(input("请输入范围n:"))
#             break
#         except:
#             print("请输入一个自然数")
#     for i in range(2, n):
#         for j in range(2, int(i**(0.5))+1):
#             if i % j == 0:
#                 break
#         else:
#             qskk.append(i)
#     return qskk
#
# print(qsk1())

'''小于给定数中能被5和7同时整除的最大数'''
# def qsk2():
#     while True:
#         try:
#             n=int(input("请输入一个自然数:"))
#             break
#         except:
#             print("输错了，请重新输入")
#     for i in range(n-1,0,-1):
#         if (i%5==0 and i%7==0):
#             # print("满足条件的最大数为：{0}".format(int(i)))
#             break
#     else:
#         print("没有满足条件的数")
#         return None
#     return i
# print(qsk2())

# def qsk3():
#     qskk3=[]
#     while True:
#         try:
#             while True:
#                 n = int(input())
#                 qskk3.append(n)
#                 q = input("要继续输入吗？").lower()
#                 if q not in {'y', 'n'}:
#                     print("请输入y(yes)或n(no)")
#                 else:
#                     break
#             if q == 'n':
#                 break
#         except:
#             print("请输入一个自然数")
#     qskkk3=[]
#     for i in qskk3:
#         j=qskk3.count(i)
#         if j==1:
#             qskkk3.append(j)
#     return qskkk3
# print(qsk3())

# def find_unique_numbers():
#     number_counts = {}  # 用于记录每个数字出现的次数
#     unique_numbers = []  # 用于存储只出现一次的数字
#
#     # 用户输入循环
#     while True:
#         try:
#             n = int(input("请输入一个数字（输入0结束）: "))
#             if n == 0:  # 用户输入0表示输入结束
#                 break
#                 # 更新数字出现次数
#             number_counts[n] = number_counts.get(n, 0) + 1
#         except ValueError:
#             print("请输入一个有效的整数。")
#             continue
#
#             # 遍历字典，找出只出现一次的数字
#     for number, count in number_counts.items():
#         if count == 1:
#             unique_numbers.append(number)
#
#     return unique_numbers
#
#
# # 调用函数并输出结果
# unique_nums = find_unique_numbers()
# print("只出现过一次的数字有:", unique_nums)


"""
第五章：函数
"""

'''斐波那契'''
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# def wfib(n):
#     a,b=1,1
#     while a<n:
#         print(a,end=" ")
#         a,b=b,a+b
# #
# def ffib (x):
#     a = 1;b = 1
#     print(1,end = " ")
#     for i in range(x):
#         print(b,end = " ")
#         a,b=b,a+b
# wfib(988);print()
# ffib(15)

# 递归，n=个数
# def fibonacci_recursive(n):
#     if n <= 0:
#         return "输入错误，请输入一个正整数。"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
#
#     # 测试代码
#
#
# print(fibonacci_recursive(10))  # 输出第10个斐波那契数

'''因式分解'''
from random import randint

# def factors(num, fac=[]):
#     #每次都从2开始查找因数
#     for i in range(2, int(num**0.5)+1):
#         #找到一个因数
#         if num%i == 0:
#             fac.append(i)
#             #对商继续分解，重复这个过程
#             factors(num//i, fac)
#             #注意，这个break非常重要
#             break
#     else:
#         #不可分解了，自身也是个因数
#         fac.append(num)
# facs = []
# n = randint(2, 10**8)
# factors(n, facs)
# result = '*'.join(map(str, facs))
# if n==eval(result):#对字符串'2*3*4'进行eval,结果等于24
#     print(n, '= '+result)

'''因式分解'''
# def factor(n):
#     if n <= 1:
#         return []  # 对于1或0，没有质因数，返回空列表
#     factors = []
#     for i in range(2, int(n ** 0.5) + 1):  # 只需要检查到sqrt(n)即可
#         while n % i == 0:
#             factors.append(i)
#             n //= i  # 使用整数除法
#     if n > 1:
#         factors.append(n)  # 如果n是质数，则它自身就是一个质因数
#     return factors


# print(factor(100))  # 应该输出质因数列表 [2, 2, 5, 5]

'''因式分解'''
# def factor(n,fac=[]):
#     if n<=1:
#         return n
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                 fac.append(n)
#                 factor(n//i,fac)
#                 break
#         else:
#             fac.append(n)
# fac1=[]
# factor(100,fac1)
# print(fac1)

'''石头剪刀布'''
# while True:
#     try:
#         n=input("请输入石头剪刀布(A/B/C)").lower()
#         d=random.choice(range(3))
#         if d==0:
#             d='a'
#         elif d==1:
#             d='b'
#         else:
#             d='c'
#         if n not in ('a','b','c'):
#             print("请输入a(石头)/b(剪刀)/c(布)")
#         elif n=='a':
#             if d=='a':
#                 print('平局')
#             elif d=='b':
#                 print('玩家获胜')
#             else:
#                 print('电脑获胜')
#         elif n=='b':
#             if d=='a':
#                 print('电脑获胜')
#             elif d == 'b':
#                 print('平局')
#             else:
#                 print('玩家获胜')
#         elif n=='c':
#             if d=='a':
#                 print('玩家获胜')
#             elif d=='b':
#                 print('电脑获胜')
#             else:
#                 print('平局')
#         while True:
#             m = input('要继续吗？').lower()
#             if m not in ('yes','no'):
#                 print('请输入yes/no')
#             else:
#                 break
#         if m=='no':
#             break
#     except:
#         print("请输入A/B/C")

import random
'''石头剪刀布'''
# while True:
#     try:
#         n = input("请输入石头、剪刀或布（A/石头, B/剪刀, C/布）: ").lower()
#
#         # 输入验证
#         if n not in ('a', 'b', 'c'):
#             print("请输入A(石头)、B(剪刀)或C(布)")
#             continue  # 继续下一次循环
#
#         # 电脑随机选择
#         d = random.choice(['a', 'b', 'c'])
#
#         # 决定胜负
#         if n == d:
#             print('平局')
#         elif (n == 'a' and d == 'b') or (n == 'b' and d == 'c') or (n == 'c' and d == 'a'):
#             print('玩家获胜！')
#         else:
#             print('电脑获胜！')
#
#             # 询问玩家是否继续
#         while True:
#             m = input('是否继续游戏？(yes/no): ').lower()
#             if m not in ('yes', 'no'):
#                 print('请输入yes或no')
#             else:
#                 break
#
#         if m == 'no':
#             break
#
#     except Exception as e:
#         print(f"出现错误: {e}")
#         print("请输入A、B或C")

'''位置参数'''
# def demo(a,b,c):
#     print(a,b,c)
# demo(1,4,5)

'''关键参数'''
# def demo(a,b,c):
#     print(a,b,c)
# demo(c=2,b=3,a=0)

'''默认值参数'''
# 任何一个带默认值参数的右边不能再有无默认值的参数，否则报错
# def demo(a=3,b):
#     print(a,b)
# demo(2)

'''可变长度参数'''
# *a将任意长度实参放入元组，**a表示字典
# def demo(*p):
#     print(p)
# demo(1,2,3,4,5)
# demo(tuple(range(10)),'end')

# def demo(**p):
#     for i in p.items():
#         print(i,end=" ")
# demo(x='x',y=2,z={})

'''序列解包'''
# def demo(a,b,c):
#     print(a+b+c)
# demo(*[1,2,3])
# demo(*(1,2,3))
# demo(*{1,2,3})
# demo(*{1:'a',2:'b',3:'c'})
# demo(*{1:'a',2:'b',3:'c'}.keys());'默认和上面一样'
# demo(*{1:'a',2:'b',3:'c'}.values())
# demo(*{1:'a',2:'b',3:'c'}.items())

'''作用域'''
# def demo():
#     global x
#     x=3;y=4
#     print('x={0},y={1}'.format(x,y))
# x=5;print(x)
# demo()
# print(x)
# del x

'''lambda'''
# a=list(range(20))
# random.shuffle(a)
# a.sort(key=lambda x:len(str(x)),reverse=True)
# print(a)

'''生成器函数'''
# yield返回值，但不会退出函数

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
# gen = simple_generator()
# print(next(gen),next(gen),next(gen))  # 输出: 1
#
# # print(next(gen))  # 输出: 1
# # print(next(gen))  # 输出: 2
# # print(next(gen))  # 输出: 3
# # print(next(gen))  # 抛出 StopIteration 异常，因为没有更多的值可以生成

# for循环遍历
# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
# for value in simple_generator():
#     print(value)  # 输出: 1, 2, 3

# def generator3(n):
#     for i in range(n):
#         if i%2==0:
#             yield i
# num3=generator3(10)
# for i in num3:
#     print(i,end=" ")

# yield解包较大数据
# def fib4():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# fib=fib4()
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# def coroutine():
#     print('Starting coroutine...')
#     x = yield
#     print('Received:', x)
#     y = yield x * 2
#     print('Received:', y)
#     yield y * 3
#
#
# coro = coroutine()
# next(coro)  # 输出: Starting coroutine...
# print(coro.send(5))  # 输出: Received: 5, 然后返回: 10
# print(coro.send(7))  # 输出: Received: 7, 然后返回: 21
# print(coro.send(10))

'''题目'''
# a=str(input())
# for i in a:
#     print(i,end=" ")

# def Aatuple():
#     low,upp=0,0
#     while True:
#         try:
#             a = str(input("请输入:"))
#             for i in a:
#                 # if i.lower()!=i or i.upper()!=i:
#                 #     break
#                 if i.lower()==i:
#                     low+=1
#                 elif i.upper()==i:
#                     upp+=1
#                 else:
#                     break
#             tuple1=(upp,low)
#             # break
#             while True:
#                 a=input("要继续输入吗?(Yes/No)")
#                 if a not in ('Yes','No'):
#                     print("请输入Yes/No")
#                 else:
#                     break
#             if a=='No':
#                 break
#         except:
#             print("你需要输入一个英文字符串:")
#     return tuple1
# print(Aatuple())


# def Aatuple():
#
#     while True:
#         low, upp = 0, 0
#         try:
#             a = str(input("请输入:"))
#
#             for i in a:
#                 if i.islower():
#                     low += 1
#                 elif i.isupper():
#                     upp += 1
#                 else:
#                     break  # 遇到非字母字符时退出循环
#
#             tuple1 = (upp, low)
#             print("当前统计结果：", tuple1)  # 在询问用户之前打印当前统计结果
#
#             while True:
#                 a = input("要继续输入吗?(Yes/No)")
#                 if a.lower() in ('yes', 'no'):  # 使用 .lower() 方法使输入不区分大小写
#                     break
#                 else:
#                     print("请输入Yes/No")
#
#             if a.lower() == 'no':
#                 break
#
#         except ValueError:  # 更具体的异常处理，仅捕获转换为字符串时的错误
#             print("你需要输入一个有效的值:")
#         except:
#             print("输入时发生错误，请确保输入的是英文字符串:")
#
#     return tuple1
#
# print(Aatuple())

'''杨辉三角'''
# def Ytrg():
#     while True:
#         try:
#             t=int(input("请输入杨辉三角的行数:"))
#             if t==0:
#                 pass
#                 break
#             elif t==1:
#                 print(1)
#                 break
#             elif t == 2:
#                 listY=[1,1]
#                 print([1])
#                 print(listY)
#                 break
#             else:
#                 print(" "*(t-1),1)
#                 listY=[1,1]
#                 print(" "*(t-2),1,1,sep=" ")
#                 for i in range(2,t):
#                     listH = []
#                     for j in range(len(listY)-1):
#                         listH.append(listY[j] + listY[j + 1])
#                     listY=[1]+listH+[1]
#                     print(" "*(t-i),end="")
#                     # for n in listY:
#                     #     if n == listY[-1]:
#                     #         print(n)
#                     #     else:
#                     #         print(n,end=" ")
#                     for n in listY:
#                         print(n,end=" ")
#                     print()
#                 break
#         except:
#             print("请输入一个自然数:")
# Ytrg()


# def yanghui(t):
#     print([1])
#     line = [1, 1]
#     print(line)
#     for i in range(2, t):
#         r = []
#         for j in range(0, len(line)-1):
#             r.append(line[j]+line[j+1])
#         line = [1]+r+[1]
#         print(line)
# print(yanghui(10))


'''输出两素数使得他们的和等于给定正偶数'''
# 1
# def ou():
#     while True:
#         try:
#             t=int(input())
#             if t%2==0 and t>0:
#                 for i in range(2,int(t/2)+1):
#                     for j in range(2,i):
#                         if i % j == 0:
#                             break
#                     else:
#                         for a in range(int(t/2)-1,t):
#                             for b in range(2,a):
#                                 if a % b == 0:
#                                     break
#                             else:
#                                 if i + a == t:
#                                     print("{0}+{1}={2}".format(i, a, t))
#             else:
#                 print("输入数字有误!")
#         except:
#             print("输入格式有误!")
# ou()

# 2
# def is_prime(n):
#     """检查一个数是否为素数"""
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def ou():
#     while True:
#         try:
#             t = int(input("请输入一个正偶数: "))
#             if t % 2 == 0 and t > 0:
#                 for i in range(2, t):
#                     if is_prime(i) and is_prime(t - i):
#                         print("{0}+{1}={2}".format(i, t - i, t))
#                         break  # 找到一组解后退出循环
#                 else:
#                     print("没有找到两个素数之和等于{0}".format(t))
#             else:
#                 print("输入数字有误，请输入一个正偶数!")
#         except ValueError:
#             print("输入格式有误，请输入一个整数!")
#         except:
#             print("发生未知错误，请重新输入!")
#
#             # 是否继续检查其他数字，这里假设不继续，直接退出循环
#         # 如果需要继续，可以删除下面的break或者替换为其他逻辑
#         break
#
#
# ou()

# 3
# def demo(n):
#     def IsPrime(p):
#         if p == 2:
#             return True
#         if p % 2 == 0:
#             return False
#         for i in range(3, int(p ** 0.5) + 1, 2):
#             if p % i == 0:
#                 return False
#         return True
#
#     if isinstance(n, int) and n > 0 and n % 2 == 0:
#         for i in range(2, n // 2 + 1):
#             if IsPrime(i) and IsPrime(n - i):
#                 print(i, '+', n - i, '=', n)
# demo(16)

'''字符串匹配率'''
# def Rate(origin, userInput):
#     if not (isinstance(origin, str) and isinstance(userInput, str)):
#         print('The two parameters must be strings.')
#         return
#     right = sum((1 for o, u in zip(origin, userInput) if o==u))
#     return round(right/len(origin), 2)
# print(Rate('origin', 'userInput'))

# origin = [1, 2, 3, 4, 5]
# userInput = [1, 2, 3, 4, 6]
#
# right = sum((1 for o, u in zip(origin, userInput) if o == u))
# accuracy = round(right / len(origin), 2)
#
# print(accuracy)  # 输出: 0.80，因为有4个元素匹配，总共5个元素



'''报数'''
from itertools import cycle

# def demo(lst, k):
#     #切片，以免影响原来的数据
#     t_lst = lst
#     #游戏一直进行到只剩下最后一个人
#     while len(t_lst)>1:
#         #创建cycle对象
#         c = cycle(t_lst)
#         #从1到k报数
#         for i in range(k):
#             t = next(c)
#         #一个人出局，圈子缩小
#         index = t_lst.index(t)
#         t_lst = t_lst[index+1:] + t_lst[:index]
#         #index后面的所有元素，在后面跟上原来第0个元素到index前一个元素
#     #游戏结束
#     return t_lst[0]
#
# lst = list(range(1,11))
# print(demo(lst, 3))

# def baoshu(list1,n):
#     list=list1
#     while len(list)>1:
#         c=cycle(list)
#         for i in range(n):
#             t=next(c)
#         index=list.index(t)
#         list=list[index+1:]+list[:index]
#     return list[0]
# print(baoshu(list(range(1,11)),3))

# list=['a','b','c','d','e','f','g']
# c=cycle(list)
# for i in range(4):
#     t=next(c)
# print(t)
# 取最后一个元素


'''汉诺塔'''
# def hannuo(num, src, dst, temp=None):
#     #声明用来记录移动次数的变量为全局变量
#     global times
#     #确认参数类型和范围
#     assert type(num) == int, 'num must be integer'
#     assert num > 0, 'num must > 0'
#     #只剩最后或只有一个盘子需要移动，这也是函数递归调用的结束条件
#     if num == 1:
#         print('The {0} Times move:{1}==>{2}'.format(times, src, dst))
#         times += 1
#     else:
#         #递归调用函数自身，
#         #先把除最后一个盘子之外的所有盘子移动到临时柱子上
#         hannuo(num-1, src, temp, dst)
#         #把最后一个盘子直接移动到目标柱子上
#         hannuo(1, src, dst)
#         #把除最后一个盘子之外的其他盘子从临时柱子上移动到目标柱子上
#         hannuo(num-1, temp, dst, src)
# #用来记录移动次数的变量
# times = 1
# #A表示最初放置盘子的柱子，C是目标柱子，B是临时柱子
# hannuo(3, 'A', 'C', 'B')

# def move(n,A,B,C):
#     if n == 1 :
#         print (A,"->",C)
#     else :
#         move(n-1,A,C,B)
#         move(1,A,B,C)
#         move(n-1,B,A,C)
# n=eval(input("请输入递归层数:"))
# move(n,'A','B','C')

# The 1 Times move:A==>C
# The 2 Times move:A==>B
# The 3 Times move:C==>B
# The 4 Times move:A==>C
# The 5 Times move:B==>A
# The 6 Times move:B==>C
# The 7 Times move:A==>C
#
#   a  b  c
# 123  0  0
# a1:move(2,A,C,B)
# a2:move(1,A,B,C)
# a3:move(2,B,A,C)
#
# a1:move(2,A,C,B)
#     b1:move(1,A,B,C)
#     b2:move(1,A,C,B)
#     b3:move(1,C,A,B)
#
# b1:move(1,A,B,C)
# n==1:print(A,-->,C)
# b2:move(1,A,C,B)
# n==1:print(a-b)
# b3:move(1,C,A,B)
# n=1:print(c-b)
#
# a2:a-c

# def hannoi(n,A,B,C):
#     if n==1:
#         print(A,'-->',C)
#     else:
#         hannoi(n-1,A,C,B)
#         hannoi(1,A,B,C)
#         hannoi(n-1,B,A,C)
# hannoi(3,'A','B','C')

""""
面向对象程序设计
"""
# class Car(object):
#     def showInfo(selfself):
#         print("This is a car.")
# car=Car()
# car.showInfo()

'''私有成员和公有成员'''
# class Test:
#     def __init__(self,value='Hello,world'):
#         self.__value=value
#         print('自动调用构造函数')
#
#     def setValue(self,value):
#         self.__value=value;'''私有数据成员'''
#
#     def show(self):
#         print(self.__value);'''公有成员函数调用私有数据成员'''
#     def __showp(self):
#         print(self.__value)
#
# t=Test()
# t.show()
# print(t._Test__value)

# _xxx   保护成员，建议通过类对象或子类对象访问，不建议通过对象直接访问
# __xxx   私有成员，只有类对象可访问，子类对象不可访问，在对象外部可以通过  Object._Class__xxx  访问
# __xxx__  特殊成员

'''数据成员'''
# 对象的数据成员:
# 在构造方法__init__()中定义,常以self作为前缀
# 只能通过对象名访问

# 类的数据成员:
# 不在任何成员方法内,该类所有对象共享,不属于任何一个对象
# 可以通过类名或对象名访问

# class SingleInstance:
#     num=0
#     def __init__(self):
#         if SingleInstance.num>0:
#             raise Exception('只能创建一个对象')
#         SingleInstance.num+=1
# t1=SingleInstance()
# t2=SingleInstance()

'''成员方法'''
# 私有方法以__开始
# 公有方法可以通过对象名直接调用，私有方法只能在其他实例方法中通过self调用或者t._Test.__xx调用
# 所有实例方法必须至少有一个self的参数，当存在多个形参时self需为第一个形参
# 在实例方法中访问成员需要以self作为前缀,但是在外部通过对象名调用对象方法时不用

'''属性'''

'''继承'''

'''特殊方法'''





"""
字符串
"""
# 不可变序列

'''编码格式'''
# AscII中1个字节表示英文，3个字节表示中文
# GB2312中1个字节表示英文，2个字节表示中文
# GB2312 GBK CP936均为2个字节表示中文
# Python3.x默认UTF-8中文为1个字节

# 字符串str--encode()编码-->字节串byte
# 字节串byte--decode()解码-->字符串str

# print(type('Python是个好语言'))
# print(type('Python是个好语言'.encode('gb2312')),type('Python是个好语言'.encode('gbk')),type('Python是个好语言'.encode('cp936')))
# print('中国'.encode())
# print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode())

'''转义字符串'''
# \b 退格，光标移动到前一格位置
# \f 换页符
# \n 换行符
# \r 回车
# \t 水平制表符
# \v 垂直制表符
# \\ 一个\
# \' 一个'
# \" 一个"
# \ooo 3位8进制对应的字符
# \xhh 2位16进制对应的字符
# \uhhhh 4位16进制表示的Unicode字符

# print("Hello\tworld")
# print('\101','\102','\103','\\103')
# print('\x41','\x42','\x58')

# def decimal_to_hex_4digits(decimal_num):
#     # 将十进制数转换为十六进制字符串
#     hex_str = hex(decimal_num)[2:]  # [2:] 去掉 '0x' 前缀
#
#     # 如果转换后的十六进制数不足4位，则在前面补零
#     hex_str = hex_str.zfill(4)
#
#     return hex_str
#
#
# decimal_number = ord('斐')
# hex_number = decimal_to_hex_4digits(decimal_number)
# print(hex_number)  # 输出应为 4 位的十六进制数
#
# print(ord('我'))
#
# print('\u6211\u662f\u9648\u6590')

# r/R原始字符串，不会转义
# a='C:\Windows\notepad.exe'
# print(a)
# a=r'C:\Users\13421\AppData\Local\Programs\Python\Python313\python.exe C:\Users\13421\AppData\Roaming\JetBrains\PyCharmCE2024.1\scratches\人工智能程序设计.py'
# print(a)

'''字符串格式化'''
# %s字符串 %c单个字符
# %d %i 10进制整数
# %o 8进制  %x 16进制
# %e 指数，基底为e
# %E 指数，基底为E
# %f %F 浮点数
# %g 指数e或浮点数
# %G 指数E或浮点数
# %%格式化为一个%

# a=1234
# print("%o" % a)
# print("%x" % a)
# print("%e" % a)

# print("%s" % 65);'''格式化为字符串，等价于str()'''
# print('%d,%c' % (68,68));'''使用元组对字符串格式化'''
# print('%s' % set(range(5)));'''把集合格式化为字符串'''

'''format()进行字符串格式化'''
# print(1/3)
# print('{0:.3f},{1:.2f}'.format(1/3,1/6));'''第一个保留3位小数，第二个2位'''
# print('{0:.3f},{0:.2f}'.format(1/3,2/3));'''0表示占位符的索引'''
# print('{0:%}'.format(3.5));'''格式化位百分数'''

# print('num d:{0:,}、{0:#d},hex:{0:#x},oct:{0:#o}'.format(10))
# print('num d:{0:,},hex:{0:x},oct:{0:o}'.format(10))
# print('The number {1} in hex is {1:#x},the number {0} in oct is {0:#o}'.format(5555,55))
# print('My name is {name},my age is {age},and my QQ is {qq}'.format(name='陈斐',age=20,qq=1933224158))

# position=(5,8,13)
# print('x:{0[0]};y:{0[1]};z:{0[2]}'.format(position))

# print('{0:_},{0:#_x},{0:#_o}'.format(10))
# print('{0:_},{0:#_x},{0:#_o}'.format(10000000))

'''格式化的字符串常量'''
# name='陈斐';age=20
# print(f'My name is {name},and my age is {age}')

# width=7;precision=4;value=11/3
# print(f'result:{value:{width}.{precision}}');'''值：{宽度}.{精确度}'''

'''find,rfind;index,rindex;count'''
# 区别：find未找到返回-1，index未找到抛出异常
# s='apple peach banana peach pear'

# print(s.find('peach'))
# print(s.find('peach',7));'''从位置7后面开始找,未找到，返回-1'''
# print(s.find('peach',7,20));'''指定范围'''
# print(s.rfind('peach',7,25));'''倒着找，返回第一个出现p的位置,start和end同find'''

# print(s.index('p'));'''返回第一次出现位置'''
# print(s.index('pe'))
# print(s.index('pear'))
# print(s.rindex('lo'));'''找不到，返回异常'''

# print(s.count('p'));'''统计p出现数量'''

'''split,rsplit,partition,rpartition'''
# s='apple peach banana pear'
# print(s.split(' '))
# print(s.split('a'))
#
# s='2024-4-28'
# print(s.split('-'))
# print(list(map(int,s.split('-'))))

# s='\n\nhello\t\t world \n\n\n My name is Dong    '
# print(s.split());'''默认以空格为分隔符，自动删除制表符'''

# a='a,,,b,,c,d'
# print(a.split(','));'''逗号中间格几个，就有几个空的元素'''

# a='a\t\t\tb\t\tc\td'
# print(a.split('\t'));'''说明了以制表符为分割，每一个制表符都是独立的符号，中间为一个空元素'''
# print(a.split());'''未说明，则直接把连续多个制表符作为一个分隔符'''

# s='\n\nhello\t\t world \n\n\n My name is Dong    '
# print(s.split(maxsplit=1))
# print(s.rsplit(maxsplit=1))
# print(s.rsplit(maxsplit=10));'''最大分隔次数大于实际可分隔次数时，自动忽略'''

# s='apple pear banana pear'
# print(s.partition('pear'));'''分隔前的部分，分隔符部分，分隔后的部分'''
# print(s.rpartition('banana'));'''从后往前第一个'''

'''join连接'''
# l=['apple','pear','banana','peach']
# print(','.join(l))
# print(' '.join(l))
# print(''.join(l))

# x='aaa     bb     c d e   fff'
# print(' '.join(x.split()))

'''lower,upper,capitalize,title,swapcase'''
# s='What is Your Name?'
# print(s.lower());'''全部小写'''
# print(s.upper());'''全部大写'''
# print(s.capitalize());'''整个字符串的首字母大写'''
# print(s.title());'''每个单词的首字母大写'''
# print(s.swapcase());'''大小写颠倒'''

'''replace,maketrans,translate'''
# print('abcdefg'.replace('abc','ABC'));'''replace每次只能替换一个字符或字符串，且不改动元字符串，二十返回一个新的字符串'''

# table = ''.maketrans('eHoldrw','1234567')
# s='Hello world'
# print(s.translate(table))

# def kaiza(l,k):
#     m = []
#     for i in range(97, 123):
#         m.append(chr(i))
#     n = ''.join(m)  # 生成26个小写字母
#     # print(n)
#     s = n[k:]+n[:k]
#     table = ''.maketrans(n,s)
#     print(l.translate(table))
# kaiza('hello world',1)

import string
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# def kaisa(s,k):
#     upper=string.ascii_uppercase
#     lower=string.ascii_lowercase
#     before=string.ascii_letters
#     after=lower[k:]+lower[:k]+upper[k:]+upper[:k]
#     table=''.maketrans(before,after)
#     print(s.translate(table))
# kaisa('abcde',3)

'''strip,rstrip,lstrip'''
# a='aaafffcccaaa'
# print(a.strip('a'))
# print(a.lstrip('a'))
# print(a.rstrip('a'))

#所删参数并不作为一个整体，而是一个字符一个字符依次向内扒
# print('aaabbcdddeefffg'.strip('bgfaedc'))

'''startswith,endswith'''
# print('Beautiful'.startswith('Be'))
# print('Beautiful'.startswith('Be',3))
# print('Beautiful'.startswith('Be',0,5))

'''isalnum数字或字母,isalpha是否字母,isdigit是否数字,isspace是否为空字符,isupper,islower'''
# print('a8'.isalnum())
# print('print'.isalpha())
# print('24433'.isdigit())#只能测试整数
# print(' '.isspace())#''不是空字符，' '是空字符
# print('ABD'.isupper())
# print('adf'.islower())

'''center居中对齐,ljust左对齐,rjust右对齐'''
# a='Hello World'
# print(a.center(20))
# print(a.center(20,'-'))
# print(a.ljust(20,'#'))
# print(a.rjust(20,'='))

'''字符串运算符'''
# print('Hello '+'world')
# print('abcd'*3)
# print('a' in 'abcd')
# print('ba' not in 'abcd')
# def alert(s):
#     if '民主' in s:
#         print('含有敏感字符!')
#     else:
#         print(s)
# alert('富强民主文明和谐')
#
# a=('拐卖','枪支','暴力','杀害')
# prime='富强民主文明和谐自由杀害'
# for i in a:
#     if i in prime:
#         prime=prime.replace(i,'***')
# print(prime)

'''内置函数'''
# s='Hello world.'
# print(list(enumerate(s)))#枚举
# print(list(zip(range(13),s)))#zip
# print(sorted(s))
# print(''.join(reversed(s)))#翻转字符串
#
# a='kunming'
# b='shenzhen'
# def add(x1,x2):
#     return x1+x2
# print(list(map(add,a,b)))
#
# print(eval('7+2*2'))
# c=3;d=9
# print(eval('c+d'))

'''字符串切片,只读'''
# a='富强民主文明和谐 自由平等公正法治爱国敬业诚信友善'
# print('Hello World'[4:])
# print(a[7:23])
# print(a[:8]+a[16:])

# print(tuple(map(str,input().split()))[::-1])

'''字符串常量'''
from random import choice
from string import ascii_letters,digits
#生成随机密码
# character=digits+ascii_letters
#
# def generator(n):
#     return ''.join(choice(character) for i in range(n))
# print(generator(8))
# print(generator(15))

'''中英文分词'''
import jieba
x='分词的准确度直接影响了后续文本处理和挖掘算法的最终效果'
# print(jieba.cut(x))
# print(list(jieba.cut(x)))
# print(' '.join(i for i in jieba.cut(x)))

import snownlp
# print(snownlp.SnowNLP('学而时习之，不亦说乎').words)
# print(snownlp.SnowNLP(x).words)

'''汉字转拼音'''
from pypinyin import lazy_pinyin,pinyin
# print(lazy_pinyin('人工智能'))
# print(lazy_pinyin('人工智能',1))
# print(lazy_pinyin('人工智能',2))
# print(lazy_pinyin('人工智能',3))
# print(lazy_pinyin('人工智能',4))
# print(lazy_pinyin('人工智能',5))
# print(lazy_pinyin('人工智能',6))
# print(lazy_pinyin('人工智能',7))
# print(lazy_pinyin('人工智能',8))
# print(lazy_pinyin('人工智能',9))
# print(lazy_pinyin('人工智能',10))#注音符号
# print(lazy_pinyin('人工智能',11))

# print(pinyin('陈斐'))
# print(pinyin('否王丁厂干',heteronym=True))

'''统计一段文字中每个词出现的个数'''
from collections import Counter
from jieba import cut
#
# def frequency(text):
#     return Counter(cut(text))
# text='''八百标兵奔北坡，北坡八百炮兵炮。
# 标兵怕碰炮兵炮，炮兵怕把标兵碰。'''
# print(list(cut(text)))
# print(frequency(text))






"""
第八章：正则表达式
"""
import re

# 常用元字符
# ^匹配以^后面的字符开头的字符串，如^http只能匹配所有以http开头的字符串
# $匹配以$前面的字符结束的字符串
# ?匹配非贪心的,如oooo,o+匹配oooo,而o+?匹配o
# \表示位于\后的转义字符
# \f匹配换页符,\n匹配换行符,\r匹配回车符
# \b匹配单词头或单词尾,\B与\b相反
# \d匹配任何数字,相当于[0-9];\D与\d相反,相当于[^0-9]
# \s匹配任何空白符,相当于[\n\f\t\v],\S与其相反
# \w匹配任何字母,数字,以及下划线,相当于[a-zA-Z0-9]
# {m,n}按照m,n进行匹配,如{3,8}表示前面的字符最少重复3次,最多重复8次


#简单的正则表达式'^......$'
#'[pjc]ython'和'(pjc)ython'都可以匹配'python','jython','cython'
# r'(http://)?(www\.)?python\.org'只能匹配'http://www.python.org','www.python.org','http://python.org','python.org'
# '(a|b)*c'匹配多个(可以是0个)a或b，后面紧跟一个c
# 'ab{1,}'等价于'ab+',匹配以a开头，后面紧跟多个b
# '[a-z]'匹配指定范围内的任何字符,'[^a-z]'匹配除a-z外的任意字符
# '^[a-zA-Z]{1}([a-zA-Z0-9._]){4,19}$'匹配长度为5-20的字符串,以一个大小写字母开头{1}且后面可带4-19个大小写字母，数字，.和_{4，19}
# '^(\w){6,20}$'匹配长度为6-20的字符串,包含字母,数字,下划线
# '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'检查是否为合法的ip地址
# '^(13[4-9]{8})|(15[01289]\d{8})$'检查是否是移动手机号
# '^\w+@(\w+\.)+\w+$'检查是否为合法邮件
# '^(\-)?\d+(\.\d{1,2})?$'检查是否为可能带有负号的带有一位或两位小数的数
# '[\u4e00-\u9fa5]'检查给定字符串中常用汉字
# '\d{4}-\d{1,2}-\d{1,2}'匹配给定格式的日期,如2024-5-16
# '^\d{18}|\d{15}$'检查是否是合法的身份证格式
# '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[,._]).{8,}$'强密码,检查是否含有字母,数字,特殊字符如,._且不少于8位
# "(?!.*[\'\"\/;=%?]).+"如果给定字符中含有' " / ; = % ?则匹配失败
# '(.)\\1+'匹配任意字符的一次或多次重复出现
# '((?P<f>\b\w+\b)\s+(?P=f))'匹配连续出现两次的单词
# '((?P<f>.)(P=f)(?P<g>.)(?P=g))'匹配AABB形式出现的成语或字母组合
# r'(\w)(?!.*\1)'查找字符串中每个字符的最后一次出现
# r'(\w)()?=.*\1'查找字符串中所有重复出现的字符

import re
# a='Please contact us at contact@xyz.com for further information. You can also write to us at feedback@xyz.com'
# print(re.findall(r'\b[\w|.%+-]+@[\w|.%+-]+\.[A-Z|a-z]{2,}\b',a))
# # print(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',a))


# text='alpha. beta....gamma delta'
# # print(re.split('[\. ]+',text))
# # print(re.split('[\. ]+',text,maxsplit=2))#最多打印两次
#
# pat='[a-zA-Z]+'#字符范围，匹配从a-z,从A-Z的所有字符
# print(re.findall(pat,text))

# pat='{name}'
# text='Dear {name}'
# re.sub(pat,'Mr.Chen',text)
# print(text)

# s='a s d'
# print(re.sub('a|s|d','good',s))
# 用good代替字符串

# s="It's a very good good idea"
# print(re.sub(r'(\b\w+) \1', r'\1', s))

# print(re.sub('a',lambda x:x.group(0).upper(),'aaa abc abde'))

# print(re.sub('a','dfg','aaa abc abde'))
# print(re.subn('a','dfg','aaa abc abde'))
# # 将'a'改为'dfg',在字符串'aaa abc abde'中

# print(re.escape('http://www.python.org'))

# match
# print(re.match('done|quit','done'))
# print(re.match('done|quit','done!'))
# print(re.match('done|quit','doe'))
# print(re.match('done|quit','d!one!'))
# print(re.search('done|quit','d!one!done'))


# example = 'Beautiful is better than ugly'
# print(re.findall('\\bb.+?\\b',example))
# print(re.findall('\\bb.+\\b',example))
# print(re.findall('\\bb\w*\\b',example))

import re
# def longest1(s):
#     t=re.findall('\d+',s)
#     if t:
#         return max(t,key=len)
#     return 'No'
#
# def longest2(s):
#     t = re.split('[^\d]+',s)
#     if t:
#         return max(t,key=len)
#     return 'No'
#
# s='123 1234 12345'
# print(longest1(s))
# print(longest2(s))

# import string
#
# def check(pwd):
#     if not isinstance(pwd,str) or len(pwd)<6:
#         return 'not suitable for password'
#
#     d={1:'weak',2:'below middle',3:'above middle',4:'strong'}
#     r=[False]*4
#
#     for ch in pwd:
#         if not r[0] and ch in string.digits:
#             r[0] = True
#         elif not r[1] and ch in string.ascii_lowercase:
#             r[1] = True
#         elif not r[2] and ch in string.ascii_uppercase:
#             r[2] = True
#         elif not r[3] and ch in ',.!;?<>':
#             r[3] = True
#     return d.get(r.count(True),'error')
# print(check('a2Cd,'),check('1234567890'),check('abcdERGJ'))


# import re
#
#
# def correct_capitalization(s):
#     # 匹配不在单词两端的大写字母
#     # pattern = r'\b[A-Z]([a-z])[A-Z]([a-z])\b'
#     pattern = r'(?<=\s)[A-Z][a-z]*(?=\s)'
#
#
#     # 使用re.sub()函数替换匹配到的大写字母为小写字母
#     corrected_s = re.sub(pattern, lambda m: m.group(0).lower(), s)
#
#     return corrected_s
#
#
# # 测试
# s = "This is a Test String with some Incorrect Capitalization."
# print(correct_capitalization(s))


"""
第9章：文件内容操作
"""


"""
爬虫
"""
# import urllib.request
# # fp=urllib.request.urlopen(r'http://www.python.org')
# # print(fp.read(100))
# # print(fp.read(100).decode)
# # fp.close()
#
# import urllib.parse
# params = urllib.parse.urlencode({'spam':1,'eggs':2,'bacon':0})
# url="http://www.python.org?%s" % params
# with urllib.request.urlopen(url) as f:
#     print(f.read().decode())

import requests



# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)	#查看网页信息，略去输出结果
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url,json=payload)
# print(r.text)	#查看网页信息，略去输出结果
# print(r.headers )	#查看头部信息，略去输出结果
# print(r.headers['Content-Type'])
# # application/json; charset=utf-8
# print(r.headers['Content-Encoding']) #Gzip

# import requests
# from bs4 import BeautifulSoup
#
# # 目标网址
# url = "https://www.chinanews.com/"
#
# # 发送请求并获取响应
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# response = requests.get(url, headers=headers)
#
# # 检查响应状态码
# if response.status_code == 200:
#     # 使用BeautifulSoup解析HTML内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 查找所有的<a>标签并提取href属性
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href:  # 确保href不为空或None
#             print(href)
# else:
#     print(f"请求失败，状态码：{response.status_code}")


#
# import re
# from bs4 import BeautifulSoup
# import requests
#
# # 目标网址
# url = "https://www.chinanews.com/"
#
# # 发送请求并获取响应
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# response = requests.get(url, headers=headers)
#
# # 检查响应状态码
# if response.status_code == 200:
#     # 使用BeautifulSoup解析HTML内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 正则表达式，匹配类似的URL
#     # 注意：这个正则表达式是简化的，可能需要根据实际情况进行调整
#     pattern = r'https://www\.chinanews\.com\.cn(/[a-zA-Z0-9-]+/)?\d{4}/\d{2}-\d{2}/[0-9]+\.shtml'
#
#     # 查找所有的<a>标签并提取href属性，使用正则表达式匹配
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href and re.match(pattern, href):
#             print(href)
# else:
#     print(f"请求失败，状态码：{response.status_code}")
