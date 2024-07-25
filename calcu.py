#calculator project
import time

Intro = "Welcome to Calculator V2,\nSupported opterations : multiplication(*), division(/), addition(+), substraction(-), modulus(%), exponents(**), floor division(//)"
print(Intro)

while True:
 AO = (input("what operation would you like to conduct?\n(+, -, /, *, %, **, //) : "))
 
 if AO=="+":
   pass
 elif AO=="-" :
   pass
 elif AO=="/" :
   pass
 elif AO=="*" :
   pass
 elif AO=="**" :
   pass
 elif AO=="%" :
   pass
 elif AO=="//" :
   pass
 else :
   print("the operation you entered is unsupported, please put in one of the support ones from the options")
   exit()
 
 n1 = eval(input("please enter the first operand : "))
 n2 = eval(input("please enter the secongd operand : "))
 
 if AO=="+" :
   ans=n1+n2
   print("{} + {} = {}".format(n1,n2,ans))
 elif AO=="-":
   ans=n1-n2
   print("{} - {} = {}".format(n1,n2,ans))
 elif AO=="*":
   ans=n1*n2
   print("{} * {} = {}".format(n1,n2,ans))
 elif AO=="/":
   ans=n1/n2
   print("{} / {} = {}".format(n1,n2,ans))
 elif AO=="//":
   ans=n1//n2
   print("{} // {} = {}".format(n1,n2,ans))
 elif AO=="**":
   ans=n1**n2
   print("{} ** {} = {}".format(n1,n2,ans))
 elif AO=="%":
   ans=n1%n2
   print("{} % {} = {}".format(n1,n2,ans))
 else :
    print("error")
 
 exit=input("please press 1 to exit and 2 to re-run...")
 if exit=="1":
   break
 elif exit=="2":
   continue
 else:
   print("invalid input, program will exit")
   time.sleep(5)
   break