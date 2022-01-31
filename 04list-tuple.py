#有序可变动列表 list
grades =[12,60,15,70,90]
print(grades[0]) #取得列表中的资料
#更新列表中的资料
grades[0]=55
print(grades)
print(grades[1:4]) #从第一个开始不包含4
#删除
grades[1:4]=[]
print(grades)
#增添
grades = grades +[12,13]
print(grades)
#取长度
print(len(grades))
#巢状的列表
data =[[3,4,5],[6,7,8]]
#取代操作
data[0][0:3]=[5,5,5]
#增加
print(data)
data[0]=data[0]+[3]
data = data +[[6,7,8]]
print(data) #第一个括号是第一个列表，第二个括号代表第一个列表的第一个数字
#有序不可变动列表 Tuple
data = (3,4,5)
print(data[0:2])
#Tuple 不可以取代，增添，删除等动作