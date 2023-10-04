class Calculator:

    def add(self, a:int, b:int):
        return a + b
    
    def sustract(self, a:int, b:int):
        return a - b
    
    def multiply(self, a:int, b:int):
        result = 0
        for i in range(a):
            result = self.add(result,b)
        return result
