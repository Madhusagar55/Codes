def get_primes(start, end):
    if start > end:
        return []

    primes = []

    for num in range(max(2, start), end + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

    return primes


start = int(input("Enter start: "))
end = int(input("Enter end: "))

print(get_primes(start, end))
