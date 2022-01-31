#定义函式
def multiply(n1,n2):
    print(n1*n2)
    return n1*n2
#呼叫函式
value = multiply(3,4)
print(value)

#程式的包装
def calculate(max=5):
    sum = 0
    for i in range(1,max+1):
        sum=sum+i
    print(sum)

calculate(10)
calculate(20)
calculate()