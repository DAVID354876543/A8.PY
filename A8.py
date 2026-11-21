print("============Power Calculator=============")

base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

result = 1

for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ": result =", result)
if exponent == 2:
    print("\nAnswer:", base, "squared is", "=", result)
elif exponent == 3:
    print("\nAnswer:", base, "cubed is", "=", result)
else:
    print("\nAnswer:", base, "to the power", exponent, "=", result)
