#资料预设
def power(base,exp=0):
        print(base**exp)
power(2)
#名称对调
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)
#程式的包装
def caculate(max):
    sum = 0
    for n in range(1,max+1):
        sum= sum+n
    print(sum)
caculate(10)
caculate(100)
#无限长度的参数