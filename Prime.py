def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Taking input
n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime")
else:
    print("Not Prime")

<<<<<<< HEAD
=======
Time complexity: O(√n)
Space complexity: O(1)
>>>>>>> ccde43cd0da7bf567f9cc533086255e835ae2adb
