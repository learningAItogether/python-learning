#集合的运算
s1={3,4,5}
print(3 not in s1)
s2={4,5,6,7}
#交集&
s3 = s1&s2
#连集|,但不重复取
s3=s1|s2
#差集-，
s3 = s2-s1 #从s2中，减去s1重叠的部分
s3 = s1-s2 #从s1中，减去s2重叠的部分
#反交集：^，取两个集合中不重叠的部分
s3 = s1^s2
print(s3)
s3 = s1
#建立集合 set(字串),无顺序性
s=set("Hello World!")
print(s)
print("H" in s)

#字典的运算
dic = {"apple":"苹果","bug":"虫虫"}
print(dic["apple"])
#修改
dic["apple"] = "小苹果"
print(dic["apple"])
# in 和 not in
print("apple" not in dic)
#删除
del dic["apple"]
print(dic)
#列表作为基础产生字典
dic={x:x*2 for x in [3,4,5]}
print(dic) 