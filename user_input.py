def main():
    name = input("What is your name? ")
    print(f"Hello, {name}!")    
    age = input("How old are you? ")
    print(f"You are {age} years old.")
    color = input("What is your favorite color? ")
    print(f"Your favorite color is {color}.")
    number1 = input("Enter a number: ")
    number2 = input("Enter another number: ")
    result = float(number1) + float(number2)
    print(f"The sum of {number1} and {number2} is {result}.")

if __name__ == "__main__":
    main()