# Your solution to Exercise 8
n = int(input(" upper limit of the range: "))
for i in range(1, n+1):
    if i % 2 != 0:
        continue
    print(i, end=" ")