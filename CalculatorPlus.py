class Calculator:
    def __init__(self):
      pass 
    
    def add(self, *args):
      sum = 0
      for each in args:
        sum += each
      return sum   
    
    def sub(self, *args):#[a-b-v-d]
      a = list(args)
      result = a[0]
      i = 1
      while i in range(len(a)):
          result = result - a[i]
          i = i + 1
      return result
          

    def mul(self, *args):
      mul = 1
      for each in args:
        mul*=each
      return mul
    
    def div(self, a,b):
      if b ==0:
         raise ValueError("cannot divide by zero")
      return a / b
                    
if __name__ == "__main__":
   cal = Calculator()
   print(f"{cal.add(16, 4,-7)}")
   print(f"{cal.sub(16, 4, -4)}")
   print(f"{cal.mul(16, 4,-1)}")
   print(f"{cal.div(16, 4)}")
    # print(f"{calculator.sqrt(16)}")
  

# I am just making these changed to check fetch.
# I am just making these changed to check fetch.