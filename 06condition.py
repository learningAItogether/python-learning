#判断式
x= input("请输入数字：") #取得字串形式的使用者输入
x = int(x)
if x>200:
    print("大于 200")
elif x>100:
    print("大于100，小于等于 200")
else:
    print("小于等于100")

#四则运算
x=int(input("请输入数字一："))
y=int(input("请输入数字二："))
op = input("请输入运算：+，-，*，/：")
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
elif op == "*":
    print(x*y)
elif op == "/":
    print(x/y)
else:
    print("不支援的运算")