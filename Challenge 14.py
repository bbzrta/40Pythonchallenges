# Fibonacci Calculator app
print("welcome to the Fibonacci Calculator App")

# Gathering information
num = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))

# Calculating the values of the fib
fib = [1, 1]
for i in range(num-2):
    fib.append(fib[i] + fib[i+1])

# Display the fib values
print("\nThe First {0} numbers of the Fibonacci sequence are: ".format(num))
print(fib)

# compute the golden ratio
golden = []
for i in range(len(fib)-1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

# Display the golden ratio value
print("\nThe corresponding Golden Ratio values are: ")
for ratio in golden:
    print(ratio)
