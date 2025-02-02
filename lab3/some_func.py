def converting(grams):
    return 28.3495231 * grams

def gradus(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))


if __name__ == "__main__":
    print()