import math



def pita():
    nitzav_1 = int(input("enter a number fo nitzav number 1":   ))
    nitzav_2 = int(input("enter a number fo nitzav number 2":   ))
    
    pita = pow(nitzav_1,2) + pow(nitzav_2,2)
    yeter = math.sqrt(pita)
    print(yeter)
pita()