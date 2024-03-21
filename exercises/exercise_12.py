# Your solution to Exercise 12
n = int(input("Enter the number n: "))
total_sum = 0
for i in range(100, 1000):
    if i % n == 0:
        total_sum += i
print(total_sum)  