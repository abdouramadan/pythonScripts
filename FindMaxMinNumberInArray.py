class FindMax:

    def __init__(self, arr):
        self.arr = arr
        self.len = len(self.arr)
        self.sum = 0

    def getMinMaxNum(self):
        maxNum =  self.arr[0] if self.arr[0] > self.arr[1] else self.arr[1]
        minNum =  self.arr[0] if self.arr[0] < self.arr[1] else self.arr[1]
        self.filterArr(minNum)
    
    def filterArr(self, minNum):
        self.arr.remove(minNum)

    def loopThroughValues(self):
        while self.sum <= 100:
            self.getMinMaxNum()
            if len(self.arr) == 1 : break
            self.sum+=1
        print('max number is : ', self.arr[0])

arr     = [100,220,3214,500,6]
findmax = FindMax(arr)
findmax.loopThroughValues()
