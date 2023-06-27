
select=int(input("select operations from 1,2,3,4:"))
num1=int(input("enter first number"))
num2=int(input("enter second number"))

if select==1:
    print(num1,"+",num2,"is" ,num1+num2)
elif select ==2:
    print(num1,"-",num2,"is" ,num1-num2)
elif select ==3:
    print(num1,"*",num2,"is" ,num1*num2)
elif select==4:
    print(num1,"/",num2,"is" ,num1/num2)
else:
    print("invalid choice")
