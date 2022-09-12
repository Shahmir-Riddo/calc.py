def addi(x,y):
    return x + y

def subs(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print(" ----- Calculator ------")
print("+", "-", "*", "/")
while True:

    choice = input(" Enter the Operator  :   ")
    p1 = int(input("Enter the first number : "))
    p2 = int(input("Enter the second number : "))

    if choice == "+":
        print("The answer is ")
        print(addi(p1,p2))


    elif choice == "-":
        print("The answer is       ")
        print(subs(p1,p2))

    elif choice == "*":

        print("The answer is    ")
        print(multiply(p1,p2))

    elif choice == "/":
        print("The answer is    ")
        print(divide)(p1,p2)

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break

    elif next_calculation == "yes":
        continue
