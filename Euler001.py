
def MULTIPLES (n):
        if  (n % 3 == 0 or n % 5 == 0):
            return True 
        else :
            return False

SUM = 0
for i in range (1, 1000):
      
        if  MULTIPLES(i) == True:
            SUM = i + SUM
print (SUM)
