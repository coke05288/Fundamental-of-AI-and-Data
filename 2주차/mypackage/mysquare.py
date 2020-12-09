
class Square:
    size = 0
    
    def __init__(self,a):
        self.size = a
        
    def getArea(self):
        result = self.size * self.size
        print("정사각형의 넓이는 : ", result)
