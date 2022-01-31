#随机模组
import random
#随机选取
data = random.choice([1,5,6,8,4,36])
print(data)

data = random.sample([1,5,6,8,4,36],5)
print(data)

#随机换顺序 / 洗牌
data = [1,5,8,4,23]
random.shuffle(data)
print(data)
#随机乱数
data = random.random()
data = random.uniform(5,19)
print(data)
#常态分布
#平均数100，标准差 10，得到的资料多数在90-110之间
#统计模组
data = []
for i in range(0,11):
    data =random.normalvariate(100,10)
    print(data)

#统计模组
import statistics as stat
data = stat.stdev([5,4,6,5])
print(data)
