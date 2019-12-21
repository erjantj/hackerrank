import heapq

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.left = []
        self.right = []

    def insert(self, number):
        if not self.left:
            self.insertLeft(number)
            self.median = number
            return
        if not self.right:
            self.insertRight(number)
            self.median = (number + self.peekLeft())/2
            return

        if number <= self.peekLeft():
            self.insertLeft(number)
        else:
            self.insertRight(number)

        if len(self.left)-len(self.right) > 1:
            self.insertRight(self.popLeft())
        elif len(self.right)-len(self.left) > 0:
            self.insertLeft(self.popRight())

        if len(self.left)-len(self.right) == 0:
            self.median = (self.peekLeft()+self.peekRight())/2
        else:
            self.median = self.peekLeft()

    def insertLeft(self, number):
        heapq.heappush(self.left, -number)

    def peekLeft(self):
        return self.left[0]*-1

    def popLeft(self):
        return heapq.heappop(self.left)*-1

    def insertRight(self, number):
        heapq.heappush(self.right, number)

    def peekRight(self):
        return self.right[0]

    def popRight(self):
        return heapq.heappop(self.right)

    def getMedian(self):
        return self.median

[1,2,3,5,10,11,12,13,100]
handler = ContinuousMedianHandler()
handler.insert(5)
handler.insert(10)
print(handler.getMedian())
handler.insert(100)
print(handler.getMedian())
handler.insert(1)
print(handler.getMedian())
handler.insert(11)
print(handler.getMedian())
handler.insert(12)
print(handler.getMedian())
handler.insert(13)
print(handler.getMedian())
handler.insert(2)
print(handler.getMedian())
handler.insert(3)
print(handler.getMedian())