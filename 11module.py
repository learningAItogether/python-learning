#载入内建的sys模组，获得咨询
import sys as s
s.path.append("modules")
print(s.platform)
print(s.maxsize)
#geomotry自建模组
import geometry
result = geometry.distance(0,0,0,5)
print(result)

result2 = geometry.slope(1,1,5,5)
print(result2)
#模组的搜寻路径
import sys as s
print(s.path)