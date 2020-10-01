# python to use calculator
while True:
    print("enter the operation you want to perform.\npress + for addition\npress - for subtraction\npress * for multilication\npress / for division\npress ^ for powering")
    comp1 = input()
    print("Enter first value")
    val1 = int(input())
    print("Enter second value")
    val2 = int(input())
    if comp1 == "+":
        print("your result is")
        print(val1 + val2 )
    elif comp1 =="-":
        print("your result is")
        print(val1 - val2 )
    elif comp1 == "*":
        print("your result is")
        print(val1 * val2 )
    elif comp1 == "/":
        print("your result is")
        print(val1/val2 )
    elif comp1 == "^":
        print("your result is")
        print(val1 ** val2 )

    else:
        print("enter correct operation")
    print("thanks for using our calculator")
