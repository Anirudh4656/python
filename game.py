import random
def gameWin(comp ,b):
    if comp==b:
         return None
    elif comp =='s':
         if b =='w':
               return False
         elif b =="g":
              return True 
    elif comp =='w':
         if b =='s':
               return False
         elif b =="g":
              return False 
    elif comp =='g':
         if b =='s':
               return False
         elif b =="w":
              return True 
randNo = random.randint(1,3)

print(randNo)
print("Comp Turn : Snake(s) water(s) or Gun(g)?")
b= input("Player's Turn : Snake(s) water(s) or Gun(g)?")
if randNo ==1:
     comp= 's'
elif randNo ==2:
     comp= 'w'
elif randNo == 3:
      comp='g'


a=gameWin(comp,b)

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
     print("You Lose")   


