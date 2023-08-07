firstNumber= float(input("input first number: "))
print(type(firstNumber))

secondNumber = float(input ("input second number: "))
print(type(secondNumber))
operator = input("which operator(1=add, 2=subtract, 3=multiply, 4=divide): ")
print("operator: ", operator)

if operator == "1":
    answer = firstNumber + secondNumber
elif operator == "2":
    answer = firstNumber - secondNumber
    
elif operator == "3":
    answer = firstNumber * secondNumber

elif operator == "4":
    answer = firstNumber / secondNumber

else: 
    print("invalid operator")

