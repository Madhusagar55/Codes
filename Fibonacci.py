Number = int(input("Enter a number:"))

a, b = 0, 1

for i in range(Number):

    print(a, end=" ")
    a, b = b, a + b