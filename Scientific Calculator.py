# %%
import math

def calculator():
    print("Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Exponential (e^x)")
    print("13. Arcsine")
    print("14. Arccosine")
    print("15. Arctangent")
    print("16. Hyperbolic Sine")
    print("17. Hyperbolic Cosine")
    print("18. Hyperbolic Tangent")
    print("19. Exit")

    while True:
        choice = input("Enter your choice (1-19): ")

        if choice == '1':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero!")
        elif choice == '5':
            num = float(input("Enter a number: "))
            if num >= 0:
                print(f"√{num} = {math.sqrt(num)}")
            else:
                print("Error: Square root of negative number!")
        elif choice == '6':
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print(f"{num1}^{num2} = {num1 ** num2}")
        elif choice == '7':
            num = float(input("Enter angle in degrees: "))
            print(f"sin({num}) = {math.sin(math.radians(num))}")
        elif choice == '8':
            num = float(input("Enter angle in degrees: "))
            print(f"cos({num}) = {math.cos(math.radians(num))}")
        elif choice == '9':
            num = float(input("Enter angle in degrees: "))
            print(f"tan({num}) = {math.tan(math.radians(num))}")
        elif choice == '10':
            num = float(input("Enter a number: "))
            if num > 0:
                print(f"log({num}) = {math.log10(num)}")
            else:
                print("Error: Logarithm of non-positive number!")
        elif choice == '11':
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                print(f"{num}! = {math.factorial(num)}")
            else:
                print("Error: Factorial of negative number!")
        elif choice == '12':
            num = float(input("Enter a number: "))
            print(f"e^{num} = {math.exp(num)}")
        elif choice == '13':
            num = float(input("Enter a number between -1 and 1: "))
            if -1 <= num <= 1:
                print(f"asin({num}) = {math.degrees(math.asin(num))}°")
            else:
                print("Error: Input out of range!")
        elif choice == '14':
            num = float(input("Enter a number between -1 and 1: "))
            if -1 <= num <= 1:
                print(f"acos({num}) = {math.degrees(math.acos(num))}°")
            else:
                print("Error: Input out of range!")
        elif choice == '15':
            num = float(input("Enter a number: "))
            print(f"atan({num}) = {math.degrees(math.atan(num))}°")
        elif choice == '16':
            num = float(input("Enter a number: "))
            print(f"sinh({num}) = {math.sinh(num)}")
        elif choice == '17':
            num = float(input("Enter a number: "))
            print(f"cosh({num}) = {math.cosh(num)}")
        elif choice == '18':
            num = float(input("Enter a number: "))
            print(f"tanh({num}) = {math.tanh(num)}")
        elif choice == '19':
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    calculator()
# %%l