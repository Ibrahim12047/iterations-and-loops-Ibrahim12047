# Your solution to Exercise 10
n = int(input("Enter the number of pounds: "))
multiplier = 0.453592
for i in range(1, n+1):
    kilograms = i * multiplier
    print(i," pounds is equal to ",kilograms,"kilograms")