def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    print("Welcome to the Fibonacci Number Generator!")
    fib_gen = fibonacci_generator()

    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate (or 0 to quit): "))
            if n == 0:
                print("Exiting...")
                break
            elif n < 0:
                print("Please enter a positive integer.")
                continue

            print(f"Generating the first {n} Fibonacci numbers:")
            fib_numbers = [next(fib_gen) for _ in range(n)]
            print(fib_numbers)
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
