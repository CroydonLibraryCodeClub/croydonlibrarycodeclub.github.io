print("Hello there")
hello=input()
print ("What is your name")
name=input()
print("How are you "+ name)
ok=input()
if ok=="bad" or ok=="not good":
  print ("Oh dear. That's bad")
  iknow=input()
  print ("Well I hope it gets sorted out")
  print (" Try to enjoy the rest of your day "+ name)
  thanks=input()
  print ("Goodbye "+ name)
  bye=input()
else:
  print ("That's good")
  print (" What day is it today "+ name)
  day=str(input())
  if day.upper() =="MONDAY":
   print ("I knew it!")
   print ("That means i have to go somewhere")
   thatsnice=input()
   print ("see you later ,weirdo whos name i cant be bothered to remember")
  else:
   print ("What, I thought it was Monday")
   print ("Are you lying to me "+ name)
   no=input()
   if no=="yes":
    print("Why would you say it is "+ name)
    explanation=input()
    print ("Well I don't care")
    huh=input()
    print("Never talk to me again in your life")
    print(" Unless you say sorry") 
    if "sorry"==input():
     print ("Ok, well I need to go. See you soon")
    else:
      print("Well I hope i never see you again. Goodbye "+name)
   