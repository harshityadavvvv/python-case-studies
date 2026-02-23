import random
print("Let the game begin")
fun=random.randint(1,100)
count=0
while(1):
  print("enter the number")
  n=int(input())
  count+=1
  if(n<fun):
    print("this number is smaller than the original number")
  elif(n>fun):
    print("this number is bigger than the original number")
  else:
    print("you wonnnnnnnnn")
    break
print("You get 5 trillion dollars and **1kg antimatter** in rewardddd")
print("the number of attempts ", count)
