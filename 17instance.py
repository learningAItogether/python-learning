#Point 实体物件的设计：平面坐标上的点
class Point:
    def __init__(self):
        self.x = 3
        self.y = 4
#第一个实体物件
p1 = Point()
print(p1.x,p1.y)
#第二个实体物件
p2 = Point()
print(p2.x,p2.y)
print("······················")
#升级
class Point1:
    def __init__(self, x,y):
        self.x = x
        self.y = y
p1 = Point1(5,6)
p2 = Point1(7,8)
print(p1.x,p1.y)
print(p2.x,p2.y)

#FullName 实体物件的设计：分开记录姓、名资料的全名
class FullName:
    def __init__(self,surName,secondName):
        self.surName = surName
        self.secondName = secondName
name1=FullName("Zhai","Xuetan")
print(name1.surName,name1.secondName)