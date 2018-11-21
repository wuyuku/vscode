# 当前房间的可用面积为： 容纳的物品有：
class home:
        def __init__(self, area):
                #当前房间的可用面积
                self.area = area
                self.contains = []
        def __str__(self):
                msg = '当前房间的可用面积为：' + self.area
                if len(self.contains > 0):
                        msg = msg + '容纳的物品有：'
                        for temp in self.contains:
                                msg = msg + temp.name + ', '
                        msg = msg.strip(', ')
                return msg
        def accomonateItems(self, items):
                neededArea = items.getUsedArea
                if self.area > neededArea:
                        self.contains.append(items)
                        self.area -= neededArea

class items:
        def __init__(self, area, name):
                self.area = area
                self.name = name
        def __str__(self):
                msg = self.name + '的面积为：'+self.area
                return msg
        def getUsedArea(self):
                return self.area