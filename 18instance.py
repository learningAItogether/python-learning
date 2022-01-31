#Point 实体物件的设计：平面坐标上的点
class Point:
    def __init__(self,x,y):
        self.x =x
        self.y =y
    #定义实体方法
    def show(self):
        print(self.x,self.y)
    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2)+((self.y-targetY)**2))**0.5
p=Point(3,4)
p.show() #呼叫实体方法 / 函式
result = p.distance(0,0) #使用
print(result)
#File实体物件的设计：包装档案读取的程式
#类：1 定义 2 初始化 3 属性/方法 4 使用 5实例
class File:
    #初始化
    def __init__(self,name):
        #属性
        self.name = name
        self.file = None
        #方法
    def open(self):
        self.file = open(self.name,mode = "r",encoding="utf-8")
    def read(self):
        return self.file.read()
#使用
f1 = File("data.text")
f1.open() #打开
result = f1.read()
print(result) #阅读

#使用2
f2 = File("data2.text")
f2.open()
data = f2.file.read()
print(data)