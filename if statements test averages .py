#If Else Test Averages by Dominique Hill

#Get Text Information from User
name=input("Enter your name")

#Define Test Average variables
Test1=76
Test2=40
Test3=98

#What is your Test average?
testaverage =eval(input("Enter your Test Average"))

#if else statements based on Test Averages
if testaverage >=90 and testaverage <=100:
   print("Hello", name, "Your test average is ", testaverage, "Your lettergrade is a A")
elif testaverage >=80 and testaverage <=89.9:
    print("Hello", name, "Your test average is ", testaverage, "Your lettergrade is a B")
elif testaverage >=70 and testaverage <=79.9:
    print("Hello", name, "Your test average is ", testaverage, "Your lettergrade is a C")
elif testaverage >=60 and testaverage <=69.9:
    print("Hello", name, "Your test average is ", testaverage, "Your lettergrade is a D")

elif testaverage <=60 and testaverage >=0:
    print("Hello", name, "Your test average is ", testaverage, "Your lettergrade is a F")

else:
    lettergrade="Incorrect Data"
    print(lettergrade)
