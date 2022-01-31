#break的简易范例
# n=0
# while n<5:
#     if n == 3:
#         break
#     print(n)
#     n+=1
# print("最后的n：",n)
#continue的简易范式
n=0
for x in [0,1,2,3]:
    if x%2==0:
        continue
    print(x)
    n+=1
print("最后的n",n)
#else的程式
sum =0
for n in range(11):
    sum = sum+n
    n+=1
else:
    print(sum)
#综合范例：找出整数平方根
#输入9，得到3
#输入11，没有整数平方根

#其他方法
n=input("please input a data:")
n=int(n)
for i in range(n):
    if i*i==n:
        print("整数平方根为：",i)
        break #强制结束回圈，不会执行else
else:
    print("没有整数平方根")