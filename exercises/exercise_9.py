# Your solution to Exercise 9
a = int(input("Enter upper num : "))
b = int(input("Enter lower num : "))
c = int(input("Enter multiple : "))

for i in range(b,a+1):
    if i % c == 0:
        print(i, end=" ")