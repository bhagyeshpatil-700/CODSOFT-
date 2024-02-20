print("_calculator_")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
print("press 1 for addition\npress 2 for subtraction\npress 3 for multiplication\npress 4 for division ")
choice = int(input("entre your choice from 1-4: "))
if choice ==1:
    result = num1+num2
    print(f"The addition of the number is: {result}  ")
elif choice ==2:
    result = num1-num2
    print(f"The subtraction of the two number is :  {result}")    
elif choice ==3:
    result = num1*num2
    print(f"The multiplication of the two number is :  {result}") 
elif choice ==4:
    result = num1/num2
    print(f"The division of the two number is :  {result}")   
print("Thank you") 
         
