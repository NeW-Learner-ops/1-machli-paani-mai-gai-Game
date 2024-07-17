def game(i):

   if int(input("Please enter the correct order:")) == i :
      print(f"{i} machli " * i)
   else :
      print("Game Over.")
      return

   if int(input("Please enter the correct order:")) == i :
      print(f"pani mai gai " * i)
   else :
      print("Game Over.")
      return

   if int(input("Please enter the correct order:")) == i :
       print(f"chappak " * i)
   else :
       print("Game Over.")
       return
   i += 1
   game(i)


   
    
x = str(input("Please enter 'start' to start the game  \n"))
if x == "start" :
   game(1)    
