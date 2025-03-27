print("welcome to my game " )

playing=input("do you want to play? ").lower()

if playing !="yes":
   quit()

print ("lets play ")
score=0
answer=input("what is CPU in full ?  ").lower()
if answer =="central processing unit":
    print("that's correct")
    score +=1
else:
    print("incorrect")

answer=input("what is GPU in full ? ").lower()
if answer =="graphics processing unit":
    print("that's correct")
    score +=1
else:
    print("incorrect")

answer=input("what is RAM in full ? ").lower()
if answer =="random access memory":
    print("that's correct")
    score +=1
else:
    print("incorrect")
    
answer=input("what is ROM in full ?  ").lower()
if answer =="read only memory":
    print("that's correct")
    score +=1
else:
    print("incorrect")

print("you got "+str(score)+" questions correct")
print("you got "+str((score/4)*100)+" %")


