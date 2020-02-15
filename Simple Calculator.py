def add(x,y):
    return x+y

def Substract(x,y):
    return x-y

def multiply(x,y):
    return x*y
 
def devide(x,y):
    return x/y

def power(x,y):
    return pow(x,y)

print("select operation.")
print("1.add")
print("2.Substract")
print("3.multiply")
print("4.devide")
print("5.power")
choice=input("Enter the choice No:1/2/3/4/5 ")

num1=int(input("Enter First No: "))
num2=int(input("Enter Second No: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice =='2':
    print(num1,"-",num2,"=", Substract(num1,num2))
    
elif choice =='3':
    print(num1,"*",num2,"=", multiply(num1,num2))
    
elif choice =='4':
    print(num1,"/",num2,"=", devide(num1,num2))
    
elif choice =='5':
    print(num1,"^",num2,"=", power(num1,num2))
    
else:
    print("Invalid input")
    
